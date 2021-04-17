// BOJ 14503 로봇 청소기
// https://www.acmicpc.net/problem/14503

import java.util.Scanner;

public class nMain {
    public static Scanner s = new Scanner(System.in);
    // Scanner 선언
    public static int d;
    // 로봇이 현재 바라보고 있는 방향 d
    public static int statusR, statusC;
    // 로봇이 있는 곳의 x 좌표, y 좌표
    public static int clean = 0;
    // 로봇이 청소하는 칸의 갯수 clean
    public static int[][] map;
    // 로봇이 있는 지도 map

    private static void createMap(int N, int M) {
        for (int i = 0; i < N ; i ++) {
            for (int j = 0; j < M ; j ++)
                map[i][j] = s.nextInt();
        }
    } // 로봇의 지도 초기화

    private static void clean() {
        map[statusR][statusC] = 2;
        clean += 1;
        search();
    } // 로봇 동작 1. 현재 위치를 청소하고 2번 시행

    private static void search() {
        leftSearch(); // 왼쪽으로 회전 후 탐색
    } // 로봇 동작 2. 탐색 진행

    private static void leftSearch() {
        turnLeft();
        robotGo(); 
        if (canNotGo()) { 
            // 청소할 공간이 없다면 2번으로 돌아가 다시 회전부터 진행함
            robotBack();
            // 사방면이 모두 막혀 있는지 확인해 볼 것
            if (noWayGo()) {
                // 사방면이 모두 막혀 있을 경우(3, 4)
                // 바라보는 방향을 유지한 채 후진을 할 수 있는가?
                robotBack();
                if (map[statusR][statusC] == 1) return;
                 // 바라보는 방향을 유지한 채 후진을 할 수 없는 경우 종료
                else robotGo();
            }
            else search();
        } 
        else clean(); // 청소할 공간이 있다면 청소하고 다시 1번부터 진행
    } // 로봇 동작 2-a. 왼쪽 탐색 진행
    
    private static void turnLeft() {
         d = (d - 1) % 4;
    } // 로봇이 왼쪽으로 회전하는 동작 turnLeft()

    private static boolean canNotGo() {
        if (map[statusR][statusC] != 0) return true;
        else return false;
    } // 로봇이 turnLeft() 한 곳으로 회전할 수 있는지 확인해 봄

    private static void robotGo() {
        if (d == 0) statusC -= 1;
        if (d == 1) statusR += 1;
        if (d == 2) statusC += 1;
        if (d == 3) statusR -= 1;
    } // 바라보고 있는 방향에 따라 전진하는 칸이 달라짐

    private static void robotBack() {
        if (d == 0) statusC += 1;
        if (d == 1) statusR -= 1;
        if (d == 2) statusC -= 1;
        if (d == 3) statusR -= 1;
    } // 로봇 동작 2-c. 네 방향 모두 갈 수 없는 경우에는 바라보는 방향 유지한 채 한 칸 후진 후 2번으로 다시 되돌아감

    private static boolean noWayGo() {
        if (map[statusR][statusC + 1] != 0  && map[statusR][statusC - 1] != 0 && map[statusR + 1][statusC] != 0 && map[statusR - 1][statusC] != 0) {
            return true;
        }
        return false;
    }

    public static void main(String[] args) {      
        int N = s.nextInt();
        int M = s.nextInt();
        map = new int[N][M];

        statusR = s.nextInt();
        statusC = s.nextInt();
        d = s.nextInt();

        createMap(N, M); // 지도 map을 규칙에 따라 생성한다.
        clean(); // 현재 있는 곳을 청소하고 2번 동작을 자동적으로 수행하는 clean() 메소드를 호출함

        System.out.println(clean); // 모든 수행을 종료한 후 몇 개의 공간을 청소했는지 출력함

        s.close();
    }
}
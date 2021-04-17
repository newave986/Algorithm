// BOJ 2447 별 찍기 10
// https://www.acmicpc.net/problem/2447

import java.util.Scanner;

public class Main {

    public static Scanner s = new Scanner(System.in);
    public static int[][] star;

    public static void starPoint(int n, int x, int y, int a, int b, int k) {

        if (x == y && a == b) return;

        if (k == 5) {
            for (int j = x; j < y; j++) {
                for (int l = a; l < b; l++) {
                    star[j][l] = 1;
                }
            }
        }
    
        starPoint(n/3, 0, n/3, 0, n/3, 1);
        starPoint(n/3, 0, n/3, n/3, 2*(n/3), 2);
        starPoint(n/3, 0, n/3, 2*(n/3), x, 3);
        starPoint(n/3, n/3, 2*(n/3), 0, n/3, 4);
        starPoint(n/3, n/3, 2*(n/3), n/3, 2*(n/3), 5);
        starPoint(n/3, n/3, 2*(n/3), 2*(n/3), n/3, 6);
        starPoint(n/3, (n/3)*2, n, 0, n/3, 7);
        starPoint(n/3, (n/3)*2, n, n/3, 2*(n/3), 8);
        starPoint(n/3, (n/3)*2, n, 2*(n/3), n, 9);
    }

    public static void main(String[] args) {
        int N = s.nextInt();
        star = new int[N][N];

        starPoint(N, 0, N, 0, N, 0);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (star[i][j] == 0) System.out.print("*");
                else System.out.print(" ");
            }
            System.out.println("");
        }
        s.close();
    }
}
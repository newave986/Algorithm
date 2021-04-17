// BOJ 2447 별 찍기 10
// https://www.acmicpc.net/problem/2447

import java.util.Scanner;
import java.util.Arrays;

public class Main {

    public static Scanner s = new Scanner(System.in);
    public static String[][] star;

    public static void starPoint(int n, int x, int a, int k) {

        if (n == 1) return;

        if (k != 10) {
            for (int j = x + (n/3); j < x + 2*(n/3); j++) {
                for (int l = a + (n/3); l < a + 2*(n/3); l++) {
                    star[j][l] = " ";
                }
            }
        }
    
        starPoint(n/3, x + 0, a + 0, 1);
        starPoint(n/3, x + 0, a + n/3, 2);
        starPoint(n/3, x + 0, a + 2*(n/3), 3);
        starPoint(n/3, x + n/3, a + 0, 4);
        starPoint(n/3, x + n/3, a + n/3, 5);
        starPoint(n/3, x + n/3, a + 2*(n/3), 6);
        starPoint(n/3, x + (n/3)*2, a + 0, 7);
        starPoint(n/3, x + (n/3)*2, a + n/3, 8);
        starPoint(n/3, x + (n/3)*2, a + 2*(n/3), 9);

    }
    
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();

        int N = s.nextInt();
        star = new String[N][N];

        for(int i = 0; i < star.length; i++) Arrays.fill(star[i], "*");

        starPoint(N, 0, 0, 0);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(star[i][j]);
            }
            if (i != N-1) sb.append("\n");
        }
        System.out.println(sb.toString());
        s.close();
    }
}
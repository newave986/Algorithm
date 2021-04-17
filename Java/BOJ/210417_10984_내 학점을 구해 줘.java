// BOJ 10984 내 학점을 구해 줘(내 학점도..)
// https://www.acmicpc.net/problem/10984

import java.util.Scanner;

public class 210417_10984{
    public static Scanner s = new Scanner(System.in);

    public static int credit;
    public static double grade;

    private static void getGrade(int x) {

        credit = 0;
        grade = 0;

        for (int i = 0; i < x; i ++) {
            int c = s.nextInt();
            credit += c;
            double g = s.nextDouble();
            grade += g * c;
        }
    }

    private static void calGrade(int n, double g) {
        grade = g / credit;
    }

    public static void main(String[] args) {

        int T = s.nextInt();
        for (int i = 0; i < T; i ++) {
            int n = s.nextInt();
            getGrade(n);
            calGrade(n, grade);
            System.out.println(credit + " " + String.format("%.1f", grade));
        }
        s.close();
    }
}
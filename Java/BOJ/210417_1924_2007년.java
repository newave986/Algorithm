// BOJ 1924 2007년
// https://www.acmicpc.net/problem/1924

import java.util.Scanner;

public class 210417_1924{
    
    private static int month(int x) {
        if (x == 1 || x == 3 || x == 5 || x == 7 || x == 8 || x == 10 || x == 12) return 31;
        if (x == 4 || x == 6 || x == 9 || x == 11) return 30;
        if (x == 2) return 28;
        return 0;
    }

    private static void dayOfWeek(int x) {
        if (x == 0) System.out.println("MON");
        if (x == 1) System.out.println("TUE");
        if (x == 2) System.out.println("WED");
        if (x == 3) System.out.println("THU");
        if (x == 4) System.out.println("FRI");
        if (x == 5) System.out.println("SAT");
        if (x == 6) System.out.println("SUN");
    }
    
    public static void main(String[] args) {
        int status = 0;

        Scanner s = new Scanner(System.in);
        int m = s.nextInt();
        int d = s.nextInt();
        for (int i = 1; i < m; i++) { 
            status += month(i);
        }
        status += d;
        dayOfWeek((status - 1) % 7);
        s.close();
    }
}
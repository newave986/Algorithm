class Solution {

    public static int Lstate = -1, Rstate = -1;
    public static String answer = "";

    public static boolean isItLeft(String hand, int n) {

        int[] firstIndex = {3, 0, 0, 0, 1, 1, 1, 2, 2, 2};
        int[] secondIndex = {1, 0, 1, 2, 0, 1, 2, 0, 1, 2};
        
        int Ldis = 0, Rdis = 0; 
        
        if (Lstate == -1) { 
            Ldis = Math.abs(3 - firstIndex[n]) + Math.abs(0 - secondIndex[n]);
            Rdis = Math.abs(firstIndex[Rstate] - firstIndex[n]) + Math.abs(secondIndex[Rstate] - secondIndex[n]);
        }
        
        else if (Rstate == -1) { 
            Ldis = Math.abs(firstIndex[Lstate] - firstIndex[n]) + Math.abs(secondIndex[Lstate] - secondIndex[n]);
            Rdis = Math.abs(3 - firstIndex[n]) + Math.abs(2 - secondIndex[n]); 
        }
    
        else {
            Ldis = Math.abs(firstIndex[Lstate] - firstIndex[n]) + Math.abs(secondIndex[Lstate] - secondIndex[n]);
            Rdis = Math.abs(firstIndex[Rstate] - firstIndex[n]) + Math.abs(secondIndex[Rstate] - secondIndex[n]);
        }
        
        if (Ldis == Rdis) {
            if (hand.equals("left")) return true;
            else return false;
            }
        else if (Ldis < Rdis) return true;
        else return false;
    }

    public static void handResult(String hand, int n) {
        if (hand.equals("left")) {
            answer += "L";
            Lstate = n;
        }
        else {
            answer += "R";
            Rstate = n;
        }
    }

    public static String solution(int[] numbers, String hand) {

        for (int i = 0; i < numbers.length; i++) {

            if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) handResult("left", numbers[i]);
            else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) handResult("right", numbers[i]);

            else {
                if (i == 0) {
                    if (hand.equals("left")) handResult("left", numbers[i]);
                    else handResult("right", numbers[i]);
                }
                else {
                    if (isItLeft(hand, numbers[i])) handResult("left", numbers[i]);
                    else handResult("right", numbers[i]);
                }
            }

        }
        return answer;
    }
}
class Solution {

    public int Lstate = 10, Rstate = 11;
    public String answer = "";

    public boolean isItLeft(String hand, int n) {

        int[] firstIndex = {3, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3};
        int[] secondIndex = {1, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 2};
    
        int Ldis = Math.abs(firstIndex[Lstate] - firstIndex[n]) + Math.abs(secondIndex[Lstate] - secondIndex[n]);
        int Rdis = Math.abs(firstIndex[Rstate] - firstIndex[n]) + Math.abs(secondIndex[Rstate] - secondIndex[n]);
        
        if (Ldis == Rdis) {
            if (hand.equals("left")) return true;
        }
        else if (Ldis < Rdis) return true;
        return false;
    }

    public void handResult(String hand, int n) {
        if (hand.equals("left")) {
            answer += "L";
            Lstate = n;
        }
        else {
            answer += "R";
            Rstate = n;
        }
    }

    public String solution(int[] numbers, String hand) {

        for (int i = 0; i < numbers.length; i++) {

            if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7) handResult("left", numbers[i]);
            else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9) handResult("right", numbers[i]);

            else {
                if (isItLeft(hand, numbers[i])) handResult("left", numbers[i]);
                else handResult("right", numbers[i]);
            }
            
        }
        
        return answer;
        
    }
}
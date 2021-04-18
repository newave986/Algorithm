# leetcode 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/

class Solution {
    private boolean palindrome(int x) {
        String y = String.valueOf(x);
        int l = y.length();

        if (1 % 2 == 0) { // 짝수일 경우
            for (int i = 0; i < l/2; i++)
                if (y.charAt(i) !=  y.charAt(l-i-1)) return false;         
        }
        else { // 홀수일 경우
            for (int i = 0; i < (int)l/2; i++) 
                if (y.charAt(i) !=  y.charAt(l-i-1)) return false;
        }
        return true;
    }
    
    public boolean isPalindrome(int x) {
        if (palindrome(x)) return true;
        else return false;
    }
}
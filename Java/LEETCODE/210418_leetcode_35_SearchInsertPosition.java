// leetcode 35. Search Insert Position
// https://leetcode.com/problems/search-insert-position/

class Solution {
    public int searchInsert(int[] nums, int target) {
        int l = nums.length;
        for (int i = 0; i < l; i++) {
            if (nums[i] == target) return i;
            else if (nums[i] > target) return i;
        }
        return l;
    }
}
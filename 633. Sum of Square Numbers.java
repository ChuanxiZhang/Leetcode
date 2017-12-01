class Solution {
    public boolean judgeSquareSum(int c) {
        int left = 0, right = (int)Math.sqrt(c);
        while (left<=right){
            int val = left * left + right * right;
            if (val < c) left++;
            else if (val > c) right--;
            else return true;
        }
    return false;
    }
}

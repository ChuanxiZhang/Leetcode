class Solution {
    public int[] productExceptSelf(int[] nums) {
        int p = 1;
        int [] res = new int[nums.length];
        for (int i = 0 ; i<nums.length; i++){
            res[i] = p;
            p = p * nums[i];
        }
        p = 1;
        for (int j = nums.length - 1; j >= 0; j--){
            res[j] = res[j] * p;
            p = p * nums[j];
        }
        return res;
    }
}

public class Solution {
    int count=0;
    public int findTargetSumWays(int[] nums, int S) {
        bfs(nums,0,0,S);
        return count;
    }
    private void bfs(int[] nums, int i, int sum, int S){
        if(i==nums.length){
            if(sum==S){
                count++;
            }
        }
        else{
            bfs(nums,i+1,sum+nums[i],S);
            bfs(nums,i+1,sum-nums[i],S);
        }

    }
}

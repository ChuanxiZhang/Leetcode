public class Solution {
    public int trap(int[] height) {
        int ans = 0;
        for ( int i = 0; i<height.length-1;i++){
            int maxleft = 0, maxright = 0;
            for (int j = i; j >= 0; j--){
                maxleft = Math.max(maxleft,height[j]);
            }
            for (int k = i; k<height.length; k++){
                maxright = Math.max(maxright,height[k]);
            }
            ans+=Math.min(maxleft,maxright)-height[i];
        }
        return ans;
    }
}

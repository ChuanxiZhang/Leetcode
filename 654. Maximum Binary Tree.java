/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return constructTree(nums,0,nums.length);
    }
    public TreeNode constructTree(int [] nums, int left, int right) {
        if (left == right) return null;
        int pos = findMaxNum(nums, left, right);
        TreeNode node = new TreeNode(nums[pos]);
        node.left = constructTree(nums,left, pos);
        node.right = constructTree(nums,pos+1, right);
        return node;
    }
    public int findMaxNum(int [] nums, int left, int right){
        int maxPos = left;
        for (int i = left ; i < right ;i++){
            if (nums[i]>nums[maxPos]) maxPos=i;
        }
        return maxPos;
    }
}

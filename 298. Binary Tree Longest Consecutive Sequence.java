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
    int maxVal = 0;
    public int longestConsecutive(TreeNode root) {
        if (root == null) return 0;
        DeepFirstSearch(root,root.val,0);
        return maxVal;
    }
    public void DeepFirstSearch(TreeNode node, int cur, int curVal){
        if(node == null) return;
        if (node.val - cur == 1) curVal++;
        else curVal = 1;
        maxVal= Math.max(maxVal,curVal);
        DeepFirstSearch(node.left,node.val, curVal);
        DeepFirstSearch(node.right,node.val, curVal);
    }
}

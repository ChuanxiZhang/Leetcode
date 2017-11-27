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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return helper(0, 0, inorder.length -1, preorder, inorder);
    }

    public TreeNode helper(int preStart, int inStart, int inEnd, int [] preorder, int [] inorder){
        int index = 0;
        if (preStart > preorder.length || inStart > inEnd){
            return null;
        }
        TreeNode root = new TreeNode(preorder[preStart]);
        for (int i = inStart ; i <= inEnd; i++){
            if (inorder[i] == root.val){
                index = i;
            }
        }
        root.left = helper(preStart + 1, inStart, index - 1 , preorder, inorder );
        root.right = helper(preStart + index - inStart + 1, index + 1, inEnd, preorder, inorder);
        return root;
    }
}

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
    public List<Integer> array  = new ArrayList<>();
    public boolean findTarget(TreeNode root, int k) {
        ToInt(root);
        HashMap<Integer,Integer> hash = new HashMap<>();
        for (int i = 0, j = array.size()-1 ; i < j;){
            if(array.get(i) + array.get(j) == k) return true;
            else if (array.get(i) + array.get(j) < k) i++;
            else j--;
        }
        return false;
    }
    public void ToInt(TreeNode node){
        if (node == null) return;
        ToInt(node.left);
        array.add(node.val);
        ToInt(node.right);
    }
}

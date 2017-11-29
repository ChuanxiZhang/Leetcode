# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, num):
            if not node.left and not node.right:
                return 10 * num + node.val
            val = 0
            if node.left:
                val += dfs(node.left, 10 * num + node.val)
            if node.right:
                val += dfs(node.right, 10 * num + node.val)
            return val

        if not root:
            return 0
        return  dfs(root, 0)

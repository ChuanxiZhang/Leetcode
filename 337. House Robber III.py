# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, memo):
            val = 0
            if not root:
                return 0
            if root in memo:
                return memo[root]
            if root.left:
                val += dfs(root.left.left, memo) + dfs(root.left.right, memo)
            if root.right:
                val += dfs(root.right.left, memo) + dfs(root.right.right, memo)
            val = max(val + root.val, dfs(root.left, memo) + dfs(root.right, memo))
            memo[root] = val
            return val
        return dfs(root,{})

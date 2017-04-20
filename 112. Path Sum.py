# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        flag=[False]
        def dfs(node, sum):
            if not node.left and not node.right:
                if sum==0:
                    flag[0]=True
            if node.left:
                dfs(node.left,sum-node.left.val)
            if node.right:
                dfs(node.right,sum-node.right.val)
        if not root:
            return False
        dfs(root,sum-root.val)
        return flag[0]
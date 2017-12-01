# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def dfs(node, parent):
            if not node:
                return 0 ,0
            li, ld = dfs(node.left, node)
            ri, rd = dfs(node.right, node)
            res[0] = max(res[0],li + rd + 1, ri + ld +1)
            if parent.val - node.val == 1:
                return 0, max(ld, rd) +1
            if parent.val - node.val == -1:
                return max(li, ri) + 1, 0
            return 0, 0
        dfs(root,root)
        return res[0]
            

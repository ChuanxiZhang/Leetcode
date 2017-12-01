# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.findLongestPath(root, res)
        return res[0]

    def findLongestPath(self, node, res):

        resl, resr = 0 ,0
        if not node:
            return 0
        left = self.findLongestPath(node.left, res)
        right = self.findLongestPath(node.right, res)

        if node.left and node.val == node.left.val:
            resl = left + 1
        if node.right and node.val == node.right.val:
            resr = right + 1
        res[0] = max(res[0], resl + resr)

        return max(resl, resr)

            

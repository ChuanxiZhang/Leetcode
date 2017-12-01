# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root,0)
        return root

    def helper(self, root, value):
        if root == None:
            return value
        right = self.helper(root.right, value)
        left = self.helper(root.left, root.val + right)
        root.val = root.val + right
        return left
            

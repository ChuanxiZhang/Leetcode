# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        def deep(n):
            if not n: return True
            return max(deep(n.left), deep(n.right)) + 1

        if not root: return True
        left = deep(root.left)
        right = deep(root.right)
        if abs(left - right) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False


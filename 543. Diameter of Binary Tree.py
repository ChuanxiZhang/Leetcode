# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        def deep(n):
            if not n:
                return 0
            left = deep(n.left)
            right = deep(n.right)
            diameter[0] = max(diameter[0], left + right)
            return max(left, right) + 1

        diameter = [0]
        deep(root)
        return diameter[0]



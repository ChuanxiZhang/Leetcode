# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        a = root.val
        kid = (root.left, root.right)[target > root.val]
        if not kid: return a
        b = self.closestValue(kid, target)
        return min((a, b), key=lambda x: abs(target - x))

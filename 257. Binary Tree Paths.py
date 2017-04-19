# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, point = stack.pop()
            if node.left:
                stack.append((node.left, point + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, point + str(node.val) + "->"))
            if not node.left and not node.right:
                res.append(point + str(node.val))
        return res

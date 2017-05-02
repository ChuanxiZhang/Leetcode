# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        arr = []

        def preOrder(node):
            if node:
                arr.append(node.val)
                preOrder(node.left)
                preOrder(node.right)

        preOrder(root)
        return arr

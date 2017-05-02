# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        arr = []

        def postOrder(node):
            if node:
                postOrder(node.left)
                postOrder(node.right)
                arr.append(node.val)

        postOrder(root)
        return arr

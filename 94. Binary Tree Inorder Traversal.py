# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        arr=[]
        def inOrder(node):
            if node:
                inOrder(node.left)
                arr.append(node.val)
                inOrder(node.right)
        inOrder(root)
        return arr
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        if not root:
            return True
        arr = []

        def inOrder(node):
            if node:
                inOrder(node.left)
                arr.append(node.val)
                inOrder(node.right)

        inOrder(root)
        return arr == sorted(arr) and len(set(arr)) == len(arr)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        sum=[0]
        def postOrder(node):
            if not node:
                return 0
            left=postOrder(node.left)
            right=postOrder(node.right)
            sum[0]+=abs(left-right)
            return left+right+node.val
        postOrder(root)
        return sum[0]
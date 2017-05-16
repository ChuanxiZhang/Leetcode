# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        if not root:
            return 0
        res = []

        def innerOrder(node):
            if node:
                innerOrder(node.left)
                res.append(node.val)
                innerOrder(node.right)

        innerOrder(root)

        minnum = min([res[i] - res[i - 1] for i in range(1, len(res))])
        return minnum

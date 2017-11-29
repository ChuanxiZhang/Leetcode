# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def right(node, depth):
            if node:
                if depth == len(res):
                    res.append(node.val)
                right(node.right, depth + 1)
                right(node.left, depth + 1)
        right(root,0)
        return res

        

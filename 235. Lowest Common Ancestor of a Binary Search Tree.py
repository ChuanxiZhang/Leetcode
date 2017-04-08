# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return root if (root.val-p.val)*(root.val-q.val)<1 else self.lowestCommonAncestor((root.left,root.right)[p.val>root.val],p,q)

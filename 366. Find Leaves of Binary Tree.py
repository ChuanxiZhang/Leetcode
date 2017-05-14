# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        if not root:
            return []
        res=[]
        def dfs(node):
            if not node:
                return 0
            deep=1+max(dfs(node.left),dfs(node.right))
            if deep==len(res)+1:
                res.append([])
            res[deep-1].append(node.val)
            return deep
        dfs(root)
        return res
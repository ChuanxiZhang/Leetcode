# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        res=[]
        def dfs(node,level):
            if node:
                if level==len(res):
                    res.insert(0,[])
                res[-(level+1)].append(node.val)
                dfs(node.left,level+1)
                dfs(node.right,level+1)
        dfs(root,0)
        return res
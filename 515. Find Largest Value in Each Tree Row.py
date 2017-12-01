# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(node, depth):
            if node:
                if depth == len(res):
                    res.append(node.val)
                else:
                    res[depth] = max(res[depth], node.val)
                dfs(node.left,depth + 1)
                dfs(node.right,depth + 1)
        dfs(root, 0)
        return res 

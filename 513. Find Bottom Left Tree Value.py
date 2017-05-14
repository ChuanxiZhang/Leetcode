# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        mostleft = [root.val]
        maxlev = [0]

        def dfs(node, level):
            if node:
                if level > maxlev[0]:
                    maxlev[0] = level
                    mostleft[0] = node.val
                dfs(node.left, level + 1)
                dfs(node.right, level + 1)

        dfs(root, 0)
        return mostleft[0]
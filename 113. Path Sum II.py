# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        res, stack = [], [root.val]

        def dfs(node, sum):
            if not node.left and not node.right:
                if sum == 0:
                    res.append(stack[:])
                return res
            if node.left:
                stack.append(node.left.val)
                dfs(node.left, sum - node.left.val)
                stack.pop()
            if node.right:
                stack.append(node.right.val)
                dfs(node.right, sum - node.right.val)
                stack.pop()

        dfs(root, sum - root.val)
        return res


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        sum = [0]
        def dfs(node, left):
            if not node: return 0
            if left:
                if not node.left and not node.right:
                    sum[0] += node.val
            dfs(node.left, True)
            dfs(node.right, False)
            return sum[0]

        return dfs(root, False)

solution=Solution()
print solution.sortedArrayToBST([1,2,3,4,5,6])
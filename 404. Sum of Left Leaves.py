# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        if
        sum = 0
        def leftsum(sum, node):
            if node.left:
                sum += node.left.val
            else:
                return leftsum(sum, node.right)

        return leftsum(sum, root)

arr=[3,9,20,0,0,15,7]
node =TreeNode()
node.root=arr[0]
for i in arr:
    node.left=

solution= Solution()
print solution.sumOfLeftLeaves(node)
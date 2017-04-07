# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        def helper(left,right):
            if left==None or right==None:
                return left == right
            if not left.val==right.val:
                return False
            return helper(left.left, right.right) and helper(left.right, right.left)
        return root == None or helper(root.left, root.right)
solution= Solution()
print solution.isSymmetric([1,2,2,3,4,4,3])
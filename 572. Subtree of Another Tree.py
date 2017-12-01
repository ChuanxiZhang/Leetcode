# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        if not s or not t:
            return False
        if s.val==t.val:
            if self.isSame(s,t):
                    return True
        return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)

    def isSame(self,big,small):
        if not big and not small:
            return True
        if not big or not small:
            return False
        if not big.val==small.val:
            return False
        return self.isSame(big.left,small.left) and self.isSame(big.right,small.right)
        

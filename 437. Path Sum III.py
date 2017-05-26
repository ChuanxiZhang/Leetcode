# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findpath(self,node,target):
        if node:
            return (node.val==target)+self.findpath(node.left,target-node.val)+self.findpath(node.right,target-node.val)
        return 0
    def pathSum(self, root, sum):
        if root:
            return self.findpath(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
        return 0
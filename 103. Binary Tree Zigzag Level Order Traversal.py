# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        stack1 = [root]
        stack2 = []
        res = []

        while stack1 or stack2:
            tmp = []
            while stack1:
                cur = stack1.pop()
                tmp.append(cur.val)
                if cur.left:
                    stack2.append(cur.left)
                if cur.right:
                    stack2.append(cur.right)
            res.append(tmp)
            tmp = []
            while stack2:
                cur = stack2.pop()
                tmp.append(cur.val)
                if cur.right:
                    stack1.append(cur.right)
                if cur.left:
                    stack1.append(cur.left)
            if tmp:
                res.append(tmp)
        return res

            

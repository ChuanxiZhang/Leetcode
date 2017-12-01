# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = [root.val]

        def rootleft(node):
            if node and (node.left or node.right):
                res.append(node.val)
                if node.left:
                    rootleft(node.left)
                elif node.right:
                    rootleft(node.right)

        def rootright(node):
            if node and (node.left or node.right):
                if node.right:
                    rootright(node.right)
                elif node.left:
                    rootright(node.left)
                res.append(node.val)

        def leaves(node):
            if node:
                if not node.left and not node.right:
                    res.append(node.val)
                leaves(node.left)
                leaves(node.right)

        rootleft(root.left)
        leaves(root.left)
        leaves(root.right)
        rootright(root.right)

        return res




            

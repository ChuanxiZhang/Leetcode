# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.arr = []
        def dfs(node):
            if node:
                dfs(node.left)
                self.arr.append(node.val)
                dfs(node.right)
        dfs(root)



    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.arr) != 0

    def next(self):
        """
        :rtype: int
        """
        return self.arr.pop(0)

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

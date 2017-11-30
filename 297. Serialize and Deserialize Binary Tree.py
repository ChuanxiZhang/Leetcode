# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        def preOrder(node):
            if node:
                vals.append(str(node.val))
                preOrder(node.left)
                preOrder(node.right)
            else:
                vals.append('*')
        vals = list()
        preOrder(root);
        return ' '.join(vals)

    def deserialize(self, data):
        def buildTree():
            val = next(vals)
            if val=='*':
                return None
            node = TreeNode(int(val))
            node.left = buildTree()
            node.right = buildTree()
            return node
        vals = iter(data.split())
        return buildTree()



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

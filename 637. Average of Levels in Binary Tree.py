# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res=[]
        counter=dict()
        def bfs(node,layer):
            if node:
                if layer in counter.keys():
                    counter[layer].append(node.val)
                else:
                    counter[layer]=[node.val]
                bfs(node.left,layer+1)
                bfs(node.right,layer+1)
        bfs(root,0)
        for i in counter.items():
            res.append(float(sum(i[1]))/float(len(i[1])))
        return res
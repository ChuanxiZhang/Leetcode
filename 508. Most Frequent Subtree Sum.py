# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        if not root:
            return []
        sumdic = dict()
        res = [0]

        def subSum(node):
            if node:
                res[0] += node.val
                subSum(node.left)
                subSum(node.right)

        def cal(root):
            if root:
                res[0] = 0
                subSum(root)
                if not sumdic.has_key(str(res[0])):
                    sumdic[str(res[0])] = 1
                else:
                    sumdic[str(res[0])] += 1
                cal(root.left)
                cal(root.right)

        cal(root)
        maxv = sorted(sumdic.iteritems(), key=lambda d: d[1], reverse=True)[0][1]
        return [int(i) for i, most in sumdic.items() if most == maxv]

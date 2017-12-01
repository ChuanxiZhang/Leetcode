# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = {}
        queue = [[root,0]]
        while queue:
            print queue
            cur = queue.pop(0)
            if cur[0]:
                if cur[1] in res:
                    res[cur[1]].append(cur[0].val)
                else:
                    res[cur[1]] = [cur[0].val]
                queue.append([cur[0].left, cur[1] - 1])
                queue.append([cur[0].right, cur[1] + 1])
        res = res.items()
        res.sort()
        return [ j for i,j in res]
        

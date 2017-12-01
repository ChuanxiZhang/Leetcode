# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res = []
        sample_counter = {}

        def helper(node):
            if not node:
                return "#"
            sample = str(node.val) + "," + helper(node.left) + "," + helper(node.right)
            if sample not in sample_counter.keys():
                sample_counter[sample] = 0
            if sample_counter[sample] == 1:
                res.append(node)
            sample_counter[sample] += 1
            return sample

        helper(root)
        return res

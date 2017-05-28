class Solution(object):
    def maxCount(self, m, n, ops):
        return min(ops)[0] * min(ops, key=lambda x: x[1])[1] if ops else m * n

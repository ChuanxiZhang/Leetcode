class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | 1 << i)
        return res

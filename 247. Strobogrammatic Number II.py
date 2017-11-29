class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.helper(n, n)

    def helper(self, n, m):
        if n == 1:
            return ['1','0','8']
        if n == 0:
            return [""]

        arr = self.helper(n - 2, m)
        res = []
        for num in arr:
            if not n == m:
                res.append('0' + num + '0')
            res.append('1' + num + '1')
            res.append('6' + num + '9')
            res.append('9' + num + '6')
            res.append('8' + num + '8')

        return res
        

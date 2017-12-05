class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right + 1):
            for d in str(i):
                if d == '0' or i % int(d) != 0:
                    break
            else:
                res.append(i)
        return res
        

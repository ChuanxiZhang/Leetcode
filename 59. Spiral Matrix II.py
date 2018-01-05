class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for _ in range(n)] for _ in range(n)]
        rs = 0
        re = n - 1
        cs = 0
        ce = n - 1
        val = 1

        while rs <= re and cs <= ce:
            for i in range(cs,ce + 1):
                res[rs][i] = val
                val += 1
            rs += 1

            for i in range(rs, re + 1):
                res[i][ce] = val
                val += 1
            ce -= 1

            for i in range(ce, cs - 1, -1):
                if rs <= re:
                    res[re][i] = val
                    val += 1
            re -= 1

            for i in range(re, rs - 1, -1):
                if cs <= ce:
                    res[i][cs] = val
                    val += 1
            cs += 1
        return res







        

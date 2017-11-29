class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        l = len(triangle)
        dp = [tri for tri in triangle[l-1]]
        top = 0
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        for i in range(l - 2, -1, -1):
            for j in range(0,i + 1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

        return dp[0]

class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(m+1)]
        for s in strs:
            zero = s.count('0')
            one = s.count('1')
            for i in range (m, zero - 1, -1):
                for j in range (n, one -1, -1):
                    dp[i][j] = max(dp[i - zero][j - one] + 1, dp[i][j])
        print dp
        return dp[m][n]

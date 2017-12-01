class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1
        if n > 10 :
            return 0
        dp = [0 for _ in range(11)]
        dp[1] = 10
        dp[2] = 81
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] * (10 - i + 1)

        return sum(dp[:n+1])
            

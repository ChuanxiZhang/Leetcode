class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[1] = 0
        for i in range(2, n + 1):
            count = i//2
            while count > 1:
                if i % count == 0:
                    dp[i] = dp[count] + i / count
                    break
                count -= 1
            else:
                dp[i] = i
        return dp[n] 

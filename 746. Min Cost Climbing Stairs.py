class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        end = len(cost) - 1
        dp = [0 for _ in range(end + 1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, end + 1):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[end], dp[end - 1])            

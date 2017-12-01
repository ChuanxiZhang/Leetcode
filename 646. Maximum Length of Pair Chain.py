class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        l = len(pairs)
        dp = [1] * len(pairs)
        pairs.sort()
        for i in range(1,l):
            for j in range(0,i):
                if pairs [i][0] > pairs[j][1]:
                    dp[i] = dp[j] + 1
        return max(dp)
        

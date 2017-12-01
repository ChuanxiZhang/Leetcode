class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        count = [1 for _ in range(len(nums))]
        res = 0
        max_len = 0
        for i in range(0,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if dp[i] == dp[j] + 1:
                        count[i] += count[j]
                    elif dp[i]< dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
            if max_len == dp[i]:
                res += count[i]
            if max_len < dp[i]:
                max_len = dp[i]
                res = count[i]
        return res




                

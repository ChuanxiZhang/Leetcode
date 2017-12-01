class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxnum = float(sum(nums[:k]))/k
        num = sum(nums[:k])
        for i in range(k,len(nums)):
            num = num - nums[i-k]+nums[i]
            val = float(num)/k
            maxnum = max(maxnum,val)
        return maxnum
            

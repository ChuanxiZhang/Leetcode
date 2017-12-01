class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        maxval = 1
        cur = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 0:
                cur += 1
                maxval = max(maxval, cur)
            else:
                cur = 1
        return maxval


            

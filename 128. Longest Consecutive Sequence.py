# nlogn
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        res = 1
        left = 0
        for i in range(1, len(nums)):
            if not nums[i] - nums[i - 1] == 1:
                res = max(res, i - left)
                left = i
        res = max(res, len(nums) - left)
        return res


            

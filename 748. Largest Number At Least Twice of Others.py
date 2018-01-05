class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        for i, num in enumerate(nums):
            if num > nums[m]:
                m = i
        for num in nums:
            if num * 2 > nums[m] and num != nums[m]:
                return -1
        return m

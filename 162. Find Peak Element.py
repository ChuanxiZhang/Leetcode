class Solution(object):
    def findPeakElement(self, nums):
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return i - 1
        return len(nums) - 1


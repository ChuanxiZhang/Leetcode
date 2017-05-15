class Solution(object):
    def findUnsortedSubarray(self, nums):
        newnums = sorted(nums)
        if nums == newnums:
            return 0
        for i in range(len(nums)):
            if not nums[i] == newnums[i]:
                break
        for j in range(len(nums) - 1, -1, -1):
            if not nums[j] == newnums[j]:
                break
        return j - i + 1


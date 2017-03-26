class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        for i in range(len(nums)):
            if target<=nums[i]:
                return i;
        else:
            return len(nums)


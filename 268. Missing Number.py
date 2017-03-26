class Solution(object):
    def missingNumber(self, nums):
        if not nums:
            return
        nums=sorted(nums)
        for i in range(len(nums)):
            if i !=nums[i]:
               return i
        else:
            return len(nums)


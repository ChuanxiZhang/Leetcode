class Solution(object):
    def moveZeroes(self, nums):
        real_i = 0
        for i in xrange(len(nums)):
            nums[real_i] = nums[i]
            if nums[i] != 0:
                real_i += 1
        for i in xrange(real_i, len(nums)):
            nums[i] = 0

        

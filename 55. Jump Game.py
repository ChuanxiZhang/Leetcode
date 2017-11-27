class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return Flase
        maxstep = 0
        for i in range(len(nums)):
            maxstep = max(maxstep - 1, nums[i])
            if maxstep == 0:
                break
        return i == len(nums) - 1
        

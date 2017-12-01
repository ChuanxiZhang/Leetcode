class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len (nums) == 0:
            return True
        false, i = 0, 1
        while i< len(nums) and false<=1:
            if nums[i-1] > nums[i]:
                false+=1
                if i-2<0 or nums[i-2]<nums[i]:nums[i-1]=nums[i]
                else: nums[i]= nums[i-1]
            i+=1
        return false<=1

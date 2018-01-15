class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        for i in range(len(nums)):
            if target - nums[i] in ht.keys():
                return [ht[target - nums[i]], i]
            else:
                ht[nums[i]] = i

class Solution(object):
    def majorityElement(self, nums):
        return max([(nums.count(num), num) for num in set(nums)])[1] if nums else None

class Solution(object):
    def thirdMax(self, nums):
        if len(set(nums))<=2:
            return max(nums)
        return sorted(set(nums))[::-1][2]
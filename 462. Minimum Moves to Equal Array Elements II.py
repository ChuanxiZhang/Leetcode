class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        return sum(nums[~i]-nums[i] for i in range(len(nums)/2))
class Solution(object):
    def findKthLargest(self, nums, k):
        return sorted(nums)[::-1][k-1]
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[0]
        if l == 0:
            return 0
        dp_max = [0] * l
        dp_min = [0] * l
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        res = nums[0]
        for i in range(1,l):
            dp_max[i] = max(max(dp_max[i-1] * nums[i], dp_min[i - 1] * nums[i]), nums[i])
            dp_min[i] = min(min(dp_max[i-1] * nums[i], dp_min[i - 1] * nums[i]), nums[i])
            res = max(res, dp_max[i])
        return res

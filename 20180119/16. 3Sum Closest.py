class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        minnum = sys.maxint
        nums.sort()
        for i in range(len(nums) - 2):
            left ,right = i + 1, len(nums) - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if abs(target - cur) < minnum:
                    res = cur
                    minnum = min(minnum, abs(target - cur))
                if cur > target:
                    right -= 1
                else:
                    left += 1
        return res

class Solution(object):
    def threeSumClosest(self, nums, target):
        close = nums[0] + nums[1] + nums[-1]
        nums.sort()
        for pos in range(len(nums) - 2):
            head, rare = pos + 1, len(nums) - 1
            while head < rare:
                sums = nums[pos] + nums[head] + nums[rare]
                if sums > target:
                    rare -= 1
                else:
                    head += 1
                if abs(target - sums) < abs(close - target):
                    close = sums
        return close





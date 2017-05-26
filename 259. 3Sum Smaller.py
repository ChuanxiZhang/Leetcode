class Solution(object):
    def threeSumSmaller(self, nums, target):
        res = 0
        nums.sort()
        for pos in range(len(nums) - 2):
            head, rare = pos + 1, len(nums) - 1
            while head < rare:
                sums = nums[pos] + nums[head] + nums[rare]
                if sums < target:
                    res += rare - head
                    head += 1
                else:
                    rare -= 1
        return res
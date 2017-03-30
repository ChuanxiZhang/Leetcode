class Solution(object):
    def twoSum(self, nums, target):
        position = dict()
        for i in range(len(nums)):
            if str(target - nums[i]) in position.keys():
                return [position[str(target - nums[i])]+1, i+1]
            else:
                position[str(nums[i])] = i
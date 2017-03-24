class Solution(object):
    def twoSum(self, nums, target):
        position = dict()
        for i in range(len(nums)):
            if str(target - nums[i]) in position.keys():
                return [position[str(target - nums[i])], i]
            else:
                position[str(nums[i])] = i


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print solution.twoSum(nums, target)

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left, right = j + 1, len(nums) - 1
                while left < right:
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    if  temp == target and [nums[i], nums[j], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif temp < target:
                        left += 1
                    else:
                        right -= 1
        return res
                        

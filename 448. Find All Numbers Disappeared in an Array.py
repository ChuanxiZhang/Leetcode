class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums=[0]+nums
        for i in range(len(nums)):
            nums[abs(nums[i])]=-abs(nums[abs(nums[i])])
        return [i for i in range(len(nums)) if nums[i]>0]


solution=Solution()
print solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])
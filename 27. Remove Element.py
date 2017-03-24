class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)
        return len(nums)
solution =Solution()
print solution.removeElement([1,2,3,3,4],3)
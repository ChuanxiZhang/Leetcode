class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

solution=Solution()
print solution.containsDuplicate("aab")
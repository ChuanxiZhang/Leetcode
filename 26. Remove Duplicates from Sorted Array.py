class Solution(object):
    def removeDuplicates(self, nums):
        nums[:]=sorted(list(set(nums)))
        return len(nums)



solution =Solution()
print solution.removeDuplicates([1,1,2])

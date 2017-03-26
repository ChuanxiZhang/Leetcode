class Solution(object):
    def findDisappearedNumbers(self, nums):
        result=list()
        if not nums:
            return []
        for i in range(len(nums)):
            if i+1 not in nums:
                result.append(i+1)
        return result
solution=Solution()
print solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if not nums:
            return 0
        count=result=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                result=max(count,result)
                count=0
        else:
            result = max(count, result)
        return result
solution= Solution()
print solution.findMaxConsecutiveOnes([1,1,0,1,1,1])
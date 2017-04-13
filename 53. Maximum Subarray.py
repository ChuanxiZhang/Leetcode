class Solution(object):
    def maxSubArray(self, nums):
        if not nums:return 0
        maxsum=sum=nums[0]
        for num in nums[1:]:
            sum=(num,sum+num)[sum>0]
            maxsum=max(maxsum,sum)
        return maxsum
solution =Solution()
print solution.maxSubArray([1,2,3,-2,4,-1])


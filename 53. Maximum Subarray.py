class Solution(object):
    def maxSubArray(self, nums):
        # if not nums:
        #     return 0
        # esum,sum=0,0
        # for i in range(len(nums)):
        #     sum=max(sum,esum)
        #     esum=0
        #     for j in range(i,len(nums)):
        #         esum=max(esum,esum+nums[j])
        # return sum
solution =Solution()
print solution.maxSubArray([1,2,3,-2,4,-1])


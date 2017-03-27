class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if not nums:
            return 0
        result=count=1
        nums="".join(map(str,nums))
        list=nums.split("0")
        if len(list)==1:
            return len(list[0])
        for i in range(len(list)-1):
            count=len(list[i]+list[i+1])+1
            result = max(count, result)
            count=0
        else:
            result = max(count, result)
        return result

solution =Solution()
print solution.findMaxConsecutiveOnes([1,1,0,1])

class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        result=list()
        for fnum in findNums:
            for i in range(len(nums)):
                if fnum==nums[i]:
                    for j in range(i,len(nums)):
                        if nums[j]>fnum:
                            result.append(nums[j])
                            break
                    else:
                        result.append(-1)
        return result
solution =Solution()
print solution.nextGreaterElement([2,4],[1,2,3,4])

class Solution(object):
    def findRelativeRanks(self, nums):
        list= sorted(nums, reverse=True)
        dic=dict()
        result= []
        for i in range(len(list)):
            if i==0:
                dic[list[i]]="Gold Medal"
            elif i==1:
                dic[list[i]] = "Silver Medal"
            elif i==2:
                dic[list[i]] = "Bronze Medal"
            else:
                dic[list[i]]=str(i+1)
        for num in nums:
            result.append(dic[num])
        return result

solution =Solution()
print solution.findRelativeRanks([5, 4, 3, 2, 1])

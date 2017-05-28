class Solution(object):
    def findLHS(self, nums):
        counts=collections.Counter(nums)
        res=0
        for count in counts:
            if count+1 in counts:
                res=max(res,counts[count]+counts[count+1])
        return res
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        for num in nums:
            below = num - 1
            if lower == below:
                res.append(str(below))
            elif lower < below:
                res.append(str(lower) + "->" + str(below))
            lower = num + 1
        if lower == upper:
            res.append(str(lower))
        elif lower < upper:
            res.append(str(lower)+'->'+ str(upper))
        return res

            

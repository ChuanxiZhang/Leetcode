class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        oneline=sum(nums,[])
        if not len(oneline)==r*c:
            return nums
        else:
            reshape= zip(*([iter(oneline)]*c))
            res=map(list,reshape)
        return res
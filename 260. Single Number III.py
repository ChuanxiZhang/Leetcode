class Solution(object):
    def singleNumber(self, nums):
        return [i for i, j in dict(collections.Counter(nums)).items() if j == 1]

class Solution(object):
    def permuteUnique(self, nums):
        return [list(a) for a in list(set(itertools.permutations(nums)))]

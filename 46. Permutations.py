class Solution(object):
    def permute(self, nums):
        return [list(a) for a in list(itertools.permutations(nums))]

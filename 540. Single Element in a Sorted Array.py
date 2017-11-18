class Solution(object):
    def singleNonDuplicate(self, nums):
        return sorted(collections.Counter(nums).items(), lambda x, y: cmp(x[1], y[1]))[0][0]

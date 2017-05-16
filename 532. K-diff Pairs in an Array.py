class Solution(object):
    def findPairs(self, nums, k):
        if k > 0:
            return len(set(nums) & set(n + k for n in nums))
        elif k == 0:
            return sum(j > 1 for j in collections.Counter(nums).values())
        else:
            return 0


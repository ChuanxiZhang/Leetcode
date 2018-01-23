class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        def backTracking(temp, pos):
            if pos >= len(nums):
                return

            for i in range(pos, len(nums)):
                temp.append(nums[i])
                if temp not in res:
                    res.append(temp[:])
                backTracking(temp, i + 1)
                temp.pop()

        backTracking([], 0)
        return res

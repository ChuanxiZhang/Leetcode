class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def backTracking(nums, n, pos):
            if len(nums) == k and n == 0:
                res.append(nums[:])
            else:
                for i in range(pos, 10):
                    if n - i >= 0:
                        if i not in nums:
                            nums.append(i)
                            backTracking(nums, n - i, i + 1)
                            nums.pop()
        backTracking([], n, 1)
        return res
                        

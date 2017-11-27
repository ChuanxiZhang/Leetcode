class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        arr = []

        def dfs(start, candidates, target):
            if target > 0:
                for i in range(start, len(candidates)):
                    if i > start and candidates[i] == candidates[i-1]:
                        continue
                    arr.append(candidates[i])
                    dfs(i + 1, candidates, target - candidates[i])
                    arr.pop()
            if target == 0:
                res.append(arr[:])

        dfs(0, candidates, target)
        return res
            

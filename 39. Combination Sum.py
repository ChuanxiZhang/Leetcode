class Solution(object):
    def combinationSum(self, candidates, target):
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
                    if target >= candidates[i]:
                        arr.append(candidates[i])
                        dfs(i, candidates, target - candidates[i])
                        arr.pop()
            if target == 0:
                res.append(arr[:])
                print res

        dfs(0, candidates, target)
        return res

                

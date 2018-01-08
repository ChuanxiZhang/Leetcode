class Solution(object):

    def __init__(self):
        self.dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        memo = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j, memo))
        return res

    def dfs(self, matrix, i, j, memo):
        if memo[i][j]:
            return memo[i][j]
        for d in self.dirs:
            x = i + d[0]
            y = j + d[1]
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                memo[i][j] = max(memo[i][j], self.dfs(matrix, x, y, memo))
        memo[i][j] += 1
        return memo[i][j]

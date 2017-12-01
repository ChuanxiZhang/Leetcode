class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return matrix
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        h, w = len(matrix), len(matrix[0])
        p_true = [[False for _ in range(w)] for _ in range(h)]
        a_true = [[False for _ in range(w)] for _ in range(h)]
        res = []

        def dfs(matrix, rec, i, j) :
                rec[i][j] = True
                for d in dirs:
                    x, y = i + d[0] , j + d[1]
                    if x < 0 or y < 0 or x >= h or y >= w or rec[x][y] or matrix[x][y] < matrix[i][j]:
                        continue
                    else:
                        dfs(matrix, rec, x, y)


        for i in range(h):
            dfs(matrix,p_true, i, 0)
            dfs(matrix,a_true, i, w-1)
        for j in range(w):
            dfs(matrix,p_true, 0, j)
            dfs(matrix,a_true, h-1, j)
        for i in range(h):
            for j in range(w):
                if p_true[i][j] and a_true[i][j]:
                    res.append([i,j])
        return res

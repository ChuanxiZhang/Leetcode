class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        q = collections.deque()
        h = len(matrix)
        w = len(matrix[0])
        for  i in range(h):
            for  j in range(w):
                if matrix[i][j] == 0:
                    q.append((i,j))
                else:
                    matrix[i][j] = sys.maxint

        def bfs(q, matrix):
            while len(q) > 0:
                cur = q.popleft()
                i, j = cur[0], cur[1]
                step = matrix[i][j] + 1
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < h and 0 <= y < w and matrix[x][y] > step:
                        matrix[x][y] = step
                        q.append((x,y))
        bfs(q, matrix)
        return matrix

    

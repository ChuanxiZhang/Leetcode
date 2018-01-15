class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cover = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = set()
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = collections.deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not cover[i][j] and grid[i][j] == 1:
                    shape = set()
                    stand = (i, j)
                    q.append([i,j])
                    shape.add((i - stand[0], j - stand[1]))
                    cover[i][j] = True
                    while q:
                        cur = q.pop()
                        a = cur[0]
                        b = cur[1]
                        shape.add((a - stand[0], b - stand[1]))
                        for d in dirs:
                            x = a + d[0]
                            y = b + d[1]
                            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1 and not cover[x][y]:
                                cover[x][y] = True
                                q.append([x,y])
                    if shape:
                        res.add(frozenset(shape))

        return len(res)

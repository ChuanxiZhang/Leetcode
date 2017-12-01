class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        cur_area = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = collections.deque()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append([i,j])
                    grid[i][j] = 0
                    while len(q) > 0:
                        i ,j = q.popleft()
                        cur_area += 1
                        for d in dirs:
                            x, y = i + d[0], j + d[1]
                            if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                                q.append([x, y])
                                grid[x][y] = 0
                    area = max(area, cur_area)
                    cur_area = 0
        return area




        

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])

        if not grid or w == 0:
            return 0

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        reached = [[0 for _ in range(w)] for _ in range(h)]
        distance = [[0 for _ in range(w)] for _ in range(h)]
        building_num = 0

        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:

                    building_num += 1
                    step = 1
                    q = collections.deque([(i,j)])
                    vst = [[False for _ in range(w)] for _ in range(h)]

                    while q:
                        for _ in range(len(q)):
                            cur = q.popleft()
                            a, b = cur[0], cur[1]
                            for d in dirs:
                                x, y = a + d[0], b + d[1]
                                if 0 <= x < h and 0 <= y < w and not vst[x][y] and grid[x][y] == 0:
                                    reached[x][y] += 1
                                    distance[x][y] += step
                                    vst[x][y] = True
                                    q.append((x,y))

                        step += 1

        res = sys.maxint
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0 and reached[i][j] == building_num:
                    res= min(res, distance[i][j])
        return res if not res == sys.maxint else -1




        

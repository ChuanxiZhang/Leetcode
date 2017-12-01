class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rowlen = len(grid)
        collen = len(grid[0]) if rowlen else 0
        rowhit, colhit, result = 0, [0] * collen, 0
        for i in range(rowlen):
            for j in range(collen):
                if not j or grid[i][j-1] == 'W':
                    rowhit = 0
                    for k in range(j,collen):
                        if grid[i][k] == 'W':
                            break
                        rowhit += grid[i][k] == 'E'
                if not i or grid[i-1][j] == 'W':
                    colhit[j]= 0
                    for k in range(i,rowlen):
                        if grid[k][j] =='W':
                            break
                        colhit[j] += (grid[k][j] == 'E')
                if grid[i][j] == '0':
                    result = max(result, colhit[j] + rowhit)
        return result

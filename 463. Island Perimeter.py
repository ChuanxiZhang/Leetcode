class Solution(object):
    def islandPerimeter(self, grid):
        island = disppear = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    island += 1
                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        disppear += 1
                    if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                        disppear += 1
        return island * 4 - disppear * 2

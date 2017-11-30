class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)

        return self.get_step(row) + self.get_step(col)

    def get_step(self, arr):
        res = 0
        left = 0
        right =len(arr) - 1
        arr.sort()
        while left < right:
            res += arr[right] - arr[left]
            left += 1
            right -= 1
        return res

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        row = 0
        col = 0
        d = 1
        h = len(matrix)
        w = len(matrix[0])
        for i in range(h * w):
            res.append(matrix[row][col])
            row -= d
            col += d

            if row == h:
                row = h - 1
                col += 2
                d = -d
            if col == w:
                col = w - 1
                row += 2
                d = -d
            if row < 0:
                row = 0
                d = -d
            if col < 0:
                col = 0
                d = -d

        return res

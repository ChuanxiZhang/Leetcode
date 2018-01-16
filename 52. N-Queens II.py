class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        chess = [('.' * n) for _ in range(n)]
        res = [0]

        def helper(chess, row, col):
            if row == n:
                res[0] += 1
            for col in range(n):
                if self.isValid(chess, row, col, n):
                    chess[row] = chess[row][:col] + 'Q' + chess[row][col + 1:]
                    helper(chess, row + 1, col)
                    chess[row] = chess[row][:col] + '.' + chess[row][col + 1:]
        helper(chess, 0, 0)
        return res[0]

    def isValid(self, chess, row, col, n):
        for i in range(row):
            if chess[i][col] == 'Q':
                return False
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chess[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if chess[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

        

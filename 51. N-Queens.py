class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        res = []
        chess = [('.' * n)  for _ in range(n)]

        def helper(row, col, n):
            if row == n:
                res.append(chess[:])
            for col in range(n):
                if self.isValid(chess, row, col, n):
                    chess[row] = chess[row][:col]+ 'Q' + chess[row][col + 1:]
                    helper(row + 1, col, n)
                    chess[row] = chess[row][:col]+ '.' + chess[row][col + 1:]

        helper(0, 0, n)
        return res

    def isValid(self, chess, row, col, n):
        for i in range(row):
            if chess[i][col] == 'Q' and i != row:
                return False
        i , j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if chess[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        i , j = row -1, col + 1
        while i >= 0 and j < n:
            if chess[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True


        

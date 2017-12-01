class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        def dfs(board, x, y):
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
                return
            if not board[x][y] == 'X':
                return
            board[x][y] = '.'
            dfs(board, x+1, y)
            dfs(board, x-1, y)
            dfs(board, x, y+1)
            dfs(board, x ,y-1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    dfs(board, i , j)
                    count += 1
        return count
            

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, x, y, word):
            if len(word) == 0:
                return True
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != word[0]:
                return False
            cur = board[x][y]
            board[x][y] = "#"
            res = dfs(board, x + 1, y, word[1:]) or dfs(board, x - 1, y, word[1:]) or dfs(board, x, y + 1, word[1:]) or dfs(board, x, y - 1, word[1:])
            board[x][y] = cur
            return res

        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False



            

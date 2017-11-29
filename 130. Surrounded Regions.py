class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if len(board) == 0:
            return
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        q = collections.deque()
        h, w = len(board), len(board[0])

        def bfs(q, board):
            while q:
                cur = q.popleft()
                i, j = cur[0], cur[1]
                board[i][j] = '1'
                for d in dirs:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < h and 0 <= y < w and board[x][y] == 'O':
                        q.append((x, y))


        for i in range(h):
            if board[i][0] =='O':
                q.append((i, 0))
            if board[i][w - 1] == 'O':
                q.append((i, w-1))

        for j in range(w):
            if board[0][j] == 'O':
                q.append((0, j))
            if board[h - 1][j] =='O':
                q.append((h-1, j))
        bfs(q, board)

        for i in range(h):
            for  j in range(w):
                if board[i][j] == '1':
                    board[i][j] = 'O'
                elif board[i][j] =='O':
                    board[i][j] = 'X'




            

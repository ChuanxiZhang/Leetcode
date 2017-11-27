class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check_row = [[False for _ in range(9)] for _ in range(9)]
        check_col = [[False for _ in range(9)] for _ in range(9)]
        check_box = [[False for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if not board[i][j] == '.':
                    num = int(board[i][j]) - 1
                    k = i / 3 * 3 + j / 3
                    if check_row[i][num] or check_col[j][num] or check_box[k][num]:
                        return False
                    check_row[i][num] = check_col[j][num] = check_box[k][num] = True
        return True

                

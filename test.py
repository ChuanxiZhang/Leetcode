class Solution(object):
    def maxCount(self, m, n, ops):
        matrix = [[0] * m] * n
        for i in range(len(ops)):
            for j in range(0, ops[i][0]):
                for k in range(0, ops[i][1]):
                    print j, k, matrix, matrix
                    matrix[0][0] += 1
        print matrix
s=Solution()
s.maxCount(3,3,[[2,2],[3,3]])

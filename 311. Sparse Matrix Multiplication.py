class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(A)
        col = len(A[0])
        res = [[0 for _ in range(len(B[0]))] for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if A[i][j] != 0:
                    for k in range(len(B[0])):
                        if B[j][k] != 0:
                            res[i][k] += A[i][j] * B[j][k]
        return res


               

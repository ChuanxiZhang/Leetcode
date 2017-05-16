class Solution(object):
    def generatePossibleNextMoves(self, s):
        res = []
        for i in range(len(s) - 1):
            if s[i] == '+' and s[i + 1] == '+':
                res.append(s[:i] + '--' + s[i + 2:])
        return res

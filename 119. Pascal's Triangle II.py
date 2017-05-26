class Solution(object):
    def getRow(self, rowIndex):
        res=[1]
        for _ in xrange(rowIndex):
            res=[x+y for x, y in zip([0]+res,res+[0])]
        return res
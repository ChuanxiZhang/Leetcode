class Solution(object):
    def findLonelyPixel(self, picture):
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B') for col in zip(*picture))

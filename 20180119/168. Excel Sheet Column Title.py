class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        if n == 0:
            return ""
        else:
            res = self.convertToTitle((n - 1) / 26) + chr((n - 1) % 26 + ord('A'))
            return res

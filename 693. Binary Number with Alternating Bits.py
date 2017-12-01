class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x = n >> 1
        y = x ^ n
        if y & y + 1 == 0:
            return True
        return False

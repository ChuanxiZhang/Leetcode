class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        cur = A
        res = 1
        while len(cur) < len(B):
            cur += A
            res += 1

        if B in cur:
            return res
        elif B in cur + A:
            return res + 1
        else:
            return -1

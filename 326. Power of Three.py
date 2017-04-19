class Solution(object):
    def isPowerOfThree(self, n):

        if n == 1:
            return True
        elif n < 3:
            return False
        while n > 1:
            if n % 3 == 0:
                n = n / 3
            else:
                return False
        return True
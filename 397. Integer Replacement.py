class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = 0
        while n != 1:
            if n % 2 == 0:
                step += 1
                n = n / 2
            elif n == 3 or bin(n - 1).count('1') < bin(n + 1).count('1'):
                step += 1
                n -= 1
            else:
                step += 1
                n += 1
        return step

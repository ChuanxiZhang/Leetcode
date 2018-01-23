class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        for i in range(L, R + 1):
            if self.isPrime(bin(i).count('1')):
                res += 1
        return res

    def isPrime(self, num):
        if num == 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
            

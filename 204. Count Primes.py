import math
class Solution(object):
    def countPrimes(self, n):
        prime=[True]*n
        if n<=2:
            return 0
        prime[:2]=[False,False]
        for i in range(2,int(((n-1)**0.5)+1)):
            if prime[i]:
                prime[i**2::i]=[False]*len(prime[i**2::i])
        return sum(prime)
solution =Solution()
print solution.countPrimes(49979)
class Solution(object):
    def isHappy(self, n):
        num = 0
        if n == 1 or n ==7: return True
        if n < 10:return False
        while n > 0:
            num += (n % 10) * (n % 10)
            n /= 10
        return self.isHappy(num)


solution = Solution()
print solution.isHappy(14)

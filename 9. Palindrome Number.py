class Solution(object):
    def isPalindrome(self, x):
        rev = 0
        y = x
        if x == 0:
            return True
        if x > 0:
            while (x != 0):
                rev = rev * 10 + x % 10
                x = x / 10
            if rev > 2147483648:
                return False
            elif rev == y:
                return True
            else:
                return False
        if x < 0:
            return False
num=12321
solution = Solution()
print solution.isPalindrome(num)

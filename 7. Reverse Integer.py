class Solution(object):
    def reverse(self, x):
        num = 0

        def rever(x, num):
            if x > 9:
                num = (num + x % 10) * 10
                return rever(x / 10, num)
            else:
                num = num + x
            if num > 2147483648:
                return 0
            else:
                return num

        if x < 0:
            return -rever(abs(x), 0)
        else:
            return rever(x, 0)


solution = Solution()
print solution.reverse(1534236469)

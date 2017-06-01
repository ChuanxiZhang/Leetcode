class Solution(object):
    def isUgly(self, num):
        for i in 2, 3, 5:
            while num % i == 0 and num > 0:
                num /= i
        return num == 1

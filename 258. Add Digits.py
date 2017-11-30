class Solution(object):
    def addDigits(self, num):
        return ( num % 9 or 9 ) if num else 0

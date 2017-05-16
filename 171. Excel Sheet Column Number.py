class Solution(object):
    def titleToNumber(self, s):
        return reduce(lambda x,y:x*26+y,[ord(i)-64 for i in s])
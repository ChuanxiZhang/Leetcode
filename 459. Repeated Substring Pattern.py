class Solution(object):
    def repeatedSubstringPattern(self, s):
        ss = (s + s)[1:-1]
        return ss.find(s) != -1

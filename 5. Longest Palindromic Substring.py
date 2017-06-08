class Solution(object):
    def longestPalindrome(self, s):
        sub = [0, 0]
        length = 0
        if len(s) < 2:
            return s
        for i in range(len(s)):
            self.extendsLetter(s, i, i, sub)
            self.extendsLetter(s, i, i + 1, sub)
        return s[sub[0]:sub[0] + sub[1]]

    def extendsLetter(self, s, start, end, sub):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
        if sub[1] < end - start - 1:
            sub[1] = end - start - 1
            sub[0] = start + 1








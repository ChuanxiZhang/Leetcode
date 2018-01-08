class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        revs = s[::-1]
        for i in range(len(s)):
            if s.startswith(revs[i:]):
                return revs[:i] + s
        return ""

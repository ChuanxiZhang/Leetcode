class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        arr = s.strip().split()
        arr.reverse()
        return " ".join(arr)

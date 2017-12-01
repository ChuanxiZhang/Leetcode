class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isValid(s, left, right - 1) or self.isValid(s, left + 1, right)
            left += 1
            right -= 1
        return True


    def isValid(self, s, left, right):
        while left < right:
            if not s[left] == s[right]:
                return False
            left += 1
            right -= 1
        return True


                

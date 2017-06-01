class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        for c in string.punctuation + " ":
            s = s.replace(c, "")
        for i in range(len(s) / 2):
            if not s[i] == s[~i]:
                return False
        return True


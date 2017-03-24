class Solution(object):
    def isValid(self, s):
        rest = len(s)
        while (rest % 2 == 0 and rest != 0):
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            rest = len(s) if rest > len(s) else 0
        return len(s) == 0


solution = Solution()
print solution.isValid("[)")

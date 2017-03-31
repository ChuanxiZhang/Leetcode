class Solution(object):
    def isAnagram(self, s, t):
        for i in s:
            if i in t:
                t = t.replace(i, '', 1)
                s = s.replace(i, '', 1)
        if t == '' and s == '':
            return True
        else:
            return False


solution=Solution()
print solution.isAnagram("aa","aab")
class Solution(object):
    def findTheDifference(self, s, t):
        for i in s:
            t=t.replace(i,'',1)
        return ''.join(t)

solution =Solution()
print solution.findTheDifference("a","aa")
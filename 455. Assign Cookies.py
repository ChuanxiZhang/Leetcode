class Solution(object):
    def findContentChildren(self, g, s):
        output=0
        sorted(g)
        sorted(s)
        for i in range(len(s)):
            for j in range(len(g)):
                if s[i]>=g[j] and g[j]>0:
                    g[j]=-g[j]
                    output+=1
                    break
        return output

solution=Solution()
print solution.findContentChildren([1,4],[3])


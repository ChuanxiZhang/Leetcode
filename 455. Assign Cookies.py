class Solution(object):
    def findContentChildren(self, g, s):
        res=0
        i=0
        s.sort()
        g.sort()
        for cookie in s:
            if i==len(g):
                break
            if cookie>=g[i]:
                i+=1
                res+=1
        return res
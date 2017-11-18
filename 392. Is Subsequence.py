class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s=="":
            return True
        pos=0
        for i in t:
            if pos==len(s):
                break
            elif s[pos]==i:
                pos+=1
        return pos==len(s)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        res = [0] * len(s)
        res[0] = 1
        count = 0
        for i in range(1,len(s)):
            for j in range(0,i):
                sub = s[j:i+1]
                if sub == sub[::-1]:
                    count += 1
            res[i] = res[i-1] + count + 1
            count = 0
        return res[len(s)-1]
        

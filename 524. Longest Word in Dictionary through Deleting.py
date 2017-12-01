class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        if not s:
            return ""
        res = ""
        for word in d:
            i,j= 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
            if j == len(word):
                if not res:
                    res = word
                else:
                    if len(word) > len(res):
                        res = word
                    elif len(word) == len(res):
                        res = min(res,word)
        return res
                    

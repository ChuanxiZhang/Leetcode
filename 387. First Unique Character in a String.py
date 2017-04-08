class Solution(object):
    def firstUniqChar(self, s):
        dic,rec = {},{}
        result=-1
        if not s:
            return -1
        for i in range(len(s)):
            if s[i] not in rec:
                dic[s[i]] = i
                rec[s[i]] = i
            elif s[i] in dic:
                del dic[s[i]]
        if dic:
            result = min(dic[pos] for pos in dic)
        return result if result>-1 else -1


solution = Solution()
print solution.firstUniqChar("abaaaab")

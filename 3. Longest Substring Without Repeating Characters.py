class Solution(object):
    def lengthOfLongestSubstring(self,s):
        start=maxlength=0
        used_char=dict()
        for i in range(len(s)):
            if s[i] in used_char and start<=used_char[s[i]]:
                start=used_char[s[i]]+1
            else:
                maxlength=max(maxlength,i-start+1)
            used_char[s[i]]=i
        return maxlength

s="abcdefbabcdefgh"
solution = Solution()
print solution.lengthOfLongestSubstring(s)
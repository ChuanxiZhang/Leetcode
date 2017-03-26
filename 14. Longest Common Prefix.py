class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        for i,item in enumerate(zip(*strs)):
            if len(set(item))>1:
                return strs[0][:i]
        else:
            return min(strs)

solution=Solution()
print solution.longestCommonPrefix(["av","abe","abc"])
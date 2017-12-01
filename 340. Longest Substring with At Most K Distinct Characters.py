class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ht = dict()
        left, res = 0, 0
        for pos, char in enumerate(s):
            ht[char] = pos
            if len(ht)>k:
                left = min(ht.values())
                del ht[s[left]]
                left += 1
            res = max(res, pos - left + 1)
        return res
            

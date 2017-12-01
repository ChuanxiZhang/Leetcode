class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) < k:
            return 0
        less = min(s, key = s.count)
        if s.count(less) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(less))

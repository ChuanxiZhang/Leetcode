class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = []
        count = 0
        cur = s[0]
        for i in range(len(s)):
            if s[i] == cur:
                count += 1
            else:
                arr.append(count)
                count = 1
                cur = s[i]
        arr.append(count)
        res = 0
        for i in range(len(arr) - 1):
            res += min(arr[i], arr[i + 1])
        return res

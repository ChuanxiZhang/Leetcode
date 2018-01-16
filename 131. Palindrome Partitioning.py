class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []

        def helper(pos,ans):
            if pos >= len(s):
                res.append(ans[:])
            else:
                for i in range(pos, len(s)):
                    if s[pos:i + 1] == s[pos: i + 1][::-1]:
                        ans.append(s[pos:i + 1])
                        helper(i + 1, ans)
                        ans.pop()

        helper(0, [])
        return res

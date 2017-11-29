class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left, right = 0, 9
        res = []
        ht = {}
        while right < len(s):
            char = s[left:right + 1]
            if char not in ht:
                ht[s[left:right + 1]] = 1
            else:
                ht[s[left:right + 1]] += 1
            left += 1
            right += 1
        return [key for key, value in ht.items() if value > 1]

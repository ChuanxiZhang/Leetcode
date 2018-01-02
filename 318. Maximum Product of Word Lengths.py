class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        w_val = [0 for _ in range(len(words))]
        res = 0

        for i, word in enumerate(words):
            for j in range(len(word)):
                w_val[i] |= 1 << (ord(word[j]) - ord('a'))
        for i in range(len(w_val)):
            for j in range(i, len(w_val)):
                if w_val[i] & w_val[j] == 0 and len(words[i]) * len(words[j]) > res:
                    res = len(words[i]) * len(words[j])
        return res

class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort(key = lambda x: (-len(x), x))
        for word in words:
            for i in range(1, len(word) + 1):
                if word[:i] not in words:
                    break
            else:
                return word
                    

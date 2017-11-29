class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.ht = collections.defaultdict(lambda:[])
        for i in range(len(words)):
            self.ht[words[i]].append(i)

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance = sys.maxint
        for i in self.ht[word1]:
            for j in self.ht[word2]:
                distance = min(distance, abs(i - j))
        return distance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

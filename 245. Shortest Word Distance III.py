class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        ht = collections.defaultdict(lambda:[])
        for i in range(len(words)):
            ht[words[i]].append(i)
        distance = sys.maxint
        if word1 == word2:
            ht[word1].sort()
            for i in range(1,len(ht[word1])):
                distance = min(distance, ht[word1][i]- ht[word1][i - 1])
            return distance if distance != sys.maxint else 0
        for i in ht[word1]:
            for j in ht[word2]:
                distance = min(distance, abs(j-i))
        return distance

        

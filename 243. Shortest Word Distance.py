class Solution(object):
    def shortestDistance(self, words, word1, word2):
        pos = [float('inf'), float('inf')]
        res = float('inf')
        for i in range(len(words)):
            if words[i] == word1:
                pos[0] = i
            if words[i] == word2:
                pos[1] = i
            res = min(res, abs(pos[1] - pos[0]))
        return res




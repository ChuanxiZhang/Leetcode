class Solution(object):
    def validWordSquare(self, words):
        return map(None, *words) == map(None, *map(None, *words))

class Solution(object):
    def isStrobogrammatic(self, num):
        return all(num[i] + num[~i] in "696001188" for i in range(len(num) / 2 + 1))

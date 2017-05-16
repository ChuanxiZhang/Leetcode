class Solution(object):
    def canPermutePalindrome(self, s):
        return sum(letter%2 for letter in collections.Counter(s).values())<2
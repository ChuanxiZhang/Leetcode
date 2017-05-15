class Solution(object):
    def distributeCandies(self, candies):
        return len(set(candies)) if len(set(candies)) < (len(candies) / 2) else (len(candies) / 2)

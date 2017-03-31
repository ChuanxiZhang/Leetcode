class Solution(object):
    def maxProfit(self, prices):
        if not prices: return 0
        low=prices[0]
        value=0
        for i in range(1,len(prices)):
            if prices[i]<low:
                low=prices[i]
            else:
                value=max(value,prices[i]-low)
        return value

solution=Solution()
print solution.maxProfit([1,2,4])


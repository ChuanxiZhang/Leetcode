class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell1, sell2 = 0 , 0
        buy1, buy2 = - sys.maxint, - sys.maxint
        for price in prices:
            sell2 = max(sell2, buy2 + price)
            buy2 = max(buy2, sell1 - price)
            sell1 = max(sell1, buy1 + price)
            buy1 = max(buy1, - price)
        return sell2



        

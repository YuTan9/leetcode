class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(len(prices)-1):
            tmp = prices[i+1] - prices[i]
            if tmp > 0:
                profit += tmp
        
        return profit
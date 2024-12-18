class Solution(object):
    def maxProfit(self, prices):
        p1 = 0 
        p2 = 1
        max_profit = 0
        
        while p1 < len(prices) and p2 < len(prices):
            max_profit = max(prices[p2] - prices[p1], max_profit)
            if prices[p1] > prices[p2]:
                p1 = p2
                p2 = p2 + 1 
            else:
                p2 = p2 + 1 
        return max_profit
                
            
        """
        :type prices: List[int]
        :rtype: int
        """
        
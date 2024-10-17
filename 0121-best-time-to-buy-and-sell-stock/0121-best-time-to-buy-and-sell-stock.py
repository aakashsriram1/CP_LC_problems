class Solution(object):
    def maxProfit(self, prices):
        p1 = 0 
        p2 = 1 
        maxx = 0 
        while p2 < len(prices): 
            price = prices[p2] - prices[p1]
            maxx = max(price,maxx)
            if prices[p2] < prices[p1]: 
                p1 = p2
                p2 = p2 + 1 
            else: 
                p2 = p2 + 1
        return maxx
        """
        :type prices: List[int]
        :rtype: int
        """
        
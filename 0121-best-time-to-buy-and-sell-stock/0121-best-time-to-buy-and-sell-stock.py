class Solution(object):
    def maxProfit(self, prices):
        ptr1 = 0 
        ptr2 = 1 
        profit = 0 
        while ptr2 < len(prices): 
            if prices[ptr1] < prices[ptr2]:
                profit = max(profit, prices[ptr2] - prices[ptr1])
            else:
                ptr1 = ptr2
            ptr2 = ptr2 + 1 
                

        return profit
            
        """
        :type prices: List[int]
        :rtype: int
        """
        
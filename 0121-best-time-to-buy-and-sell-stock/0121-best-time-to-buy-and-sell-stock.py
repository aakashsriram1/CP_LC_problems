class Solution(object):
    def maxProfit(self, prices):
        left_ptr = 0 
        right_ptr = 1
        val = 0 
        
        while right_ptr < len(prices):
            if prices[left_ptr] < prices[right_ptr]:
                val = max(val,prices[right_ptr] - prices[left_ptr])
            else: 
                left_ptr = right_ptr
            right_ptr = right_ptr + 1 
        return val
            
            
            
        
        """
        :type prices: List[int]
        :rtype: int
        """
        
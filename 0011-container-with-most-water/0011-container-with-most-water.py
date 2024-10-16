class Solution(object):
    def maxArea(self, height):
        res = 0 
        l = 0 
        r = len(height) - 1 
        while l < r:
            calculated_value = min(height[l],height[r]) * (r - l) 
            res = max(res,calculated_value)
            if height[l] > height[r]: 
                r = r - 1 
            elif height[r] > height[l]: 
                l = l + 1 
            else:
                r = r - 1
        return res 
            
            
            
            
            
            
        
        """
        :type height: List[int]
        :rtype: int
        """
        
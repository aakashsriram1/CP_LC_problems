class Solution(object):
    def search(self, nums, target):
        l = 0 
        r = len(nums) - 1
        while l <= r: 
            m = (l+r) // 2
            if(nums[m] == target): 
                return m 
            elif(nums[m] > target): 
                r = m - 1 
            elif(nums[m] < target): 
                l = m + 1 
        return -1 
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
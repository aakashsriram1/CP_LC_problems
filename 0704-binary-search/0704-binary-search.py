class Solution(object):
    def search(self, nums, target):
        p1 = 0 
        p2 = len(nums) -1 
        
        while p1 <= p2: 
            m = (p1 + p2) // 2
            if nums[m] == target:
                return m 
            elif nums[m] > target:
                p2 = m - 1 
            elif nums[m] < target: 
                p1 = m + 1
        return -1
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
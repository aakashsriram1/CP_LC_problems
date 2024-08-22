class Solution(object):
    def maxSubArray(self, nums):
        max_val = -999999999 
        curr_sum = 0 
        for i in range(len(nums)): 
            curr_sum += nums[i]
            max_val = max(max_val,curr_sum)
            if curr_sum < 0: 
                curr_sum = 0 
        return max_val
        """
        :type nums: List[int]
        :rtype: int
        """
        
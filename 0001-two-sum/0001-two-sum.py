class Solution(object):
    def twoSum(self, nums, target):
        hashset = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashset: 
                return [hashset[complement],i]
            hashset[nums[i]] = i
            
            
            
            
            
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
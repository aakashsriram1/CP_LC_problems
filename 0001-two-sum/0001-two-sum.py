class Solution(object):
    def twoSum(self, nums, target):
        dictionary = {}
        
        for i in range(len(nums)): 
            complement = target - nums[i] 
            if complement in dictionary: 
                return [dictionary[complement], i]
            dictionary[nums[i]] = i
            
        
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
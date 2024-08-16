class Solution(object):
    def twoSum(self, nums, target):
        mapped_values = {}

        for i in range(len(nums)): 
            complement = target - nums[i]
            if complement in mapped_values:
                return [mapped_values[complement], i]
            mapped_values[nums[i]] = i 

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
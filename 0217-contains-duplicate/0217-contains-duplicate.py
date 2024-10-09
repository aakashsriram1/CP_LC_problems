class Solution(object):
    def containsDuplicate(self, nums):
        dictionary = {}
        for i in range(len(nums)):
            if nums[i] in dictionary: 
                return True
            dictionary[nums[i]] = dictionary.get(i,0)
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        
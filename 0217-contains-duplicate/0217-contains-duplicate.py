class Solution(object):
    def containsDuplicate(self, nums):
        dictionary = {}
        for i in nums: 
            if i in dictionary: 
                return True
            dictionary[i] = dictionary.get(i,0) + 1 
        return False
            
        """"
        :type nums: List[int]
        :rtype: bool
        """
    
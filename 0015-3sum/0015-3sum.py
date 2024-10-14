class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        output = []
        
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index-1]:
                continue
            p1 = index + 1
            p2 = len(nums) -1 
            while p1 < p2: 
                target = value + nums[p1] + nums[p2]
                if target > 0:
                    p2 = p2  - 1
                elif target < 0:
                    p1 = p1 + 1 
        
                else:
                    output.append([value,nums[p1],nums[p2]])
                    p1 = p1+1 
                    while nums[p1] == nums[p1 - 1] and p1 < p2: 
                        p1 = p1 + 1
        return output


        #-4 -1 -1 0 1 2 
        #-4 + 2 = -2
            
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
class Solution(object):
    def twoSum(self, numbers, target):
        p1 = 0 
        p2 = len(numbers) - 1 
        while p1 < p2: 
            total = numbers[p1] + numbers[p2]
            if total > target: 
                p2 = p2 -1 
            elif total < target: 
                p1 = p1 + 1 
            elif total == target:
                return [p1 + 1,p2 + 1]
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
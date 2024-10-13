class Solution(object):
    def topKFrequent(self, nums, k):
        n = len(nums)
        dictionary = {}
        
        for i in nums: 
            dictionary[i] = dictionary.get(i,0) + 1 
            
        buckets = [0] * (n + 1)
        for num,freq in dictionary.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        ret = []
        for i in range(n,0,-1):
                if buckets[i]:
                    for num in buckets[i]:
                        ret.append(num)
                        if len(ret) == k:
                            return ret
        return ret
                
                
                
            
                 

            
            
        
        

            
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
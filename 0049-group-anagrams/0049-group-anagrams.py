class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        for i in strs:
            sortedI = ''.join(sorted(i))
            if sortedI not in hashmap: 
                hashmap[sortedI] = [i]
            else:
                hashmap[sortedI].append(i)
        return hashmap.values()
            
                

            
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
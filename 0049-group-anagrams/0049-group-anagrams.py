class Solution(object):
    def groupAnagrams(self, strs):
        hashset = {}
        for i in strs: 
            key = ''.join(sorted(i))
            if key not in hashset:
                hashset[key] = []
            hashset[key].append(i)
        return hashset.values()
            
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
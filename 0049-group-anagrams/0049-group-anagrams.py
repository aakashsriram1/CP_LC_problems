class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        for i in strs: 
            txt = ''.join(sorted(i))
            if txt in hashmap:
                hashmap[txt] += [i]
            else:
                hashmap[txt] = [i]
        return hashmap.values()
                

            
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
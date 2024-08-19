class Solution(object):
    def isAnagram(self, s, t):
        word_map_s = {}
        word_map_t = {}
        
        if len(s) != len(t): 
            return False
        for i in range(len(s)): 
            word_map_s[s[i]] = word_map_s.get(s[i],0) + 1 
            word_map_t[t[i]] = word_map_t.get(t[i],0) + 1 
        return word_map_s == word_map_t
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
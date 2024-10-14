class Solution(object):
    def isPalindrome(self, s):
        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            
            if s[p1].isalnum() == False:
                p1 = p1 + 1
                
            elif s[p2].isalnum() == False:
                p2 = p2 - 1      
                
            elif s[p1].lower() == s[p2].lower():
                p1 = p1 + 1
                p2 = p2 - 1
                
            else:
                return False
        return True
        """
        :type s: str
        :rtype: bool
        """
        
class Solution(object):
    def isValid(self, s):
        stack = []
        connections_map = {'}':'{', ']':'[',  ')':'('}
        
        for i in s: 
            if i in connections_map: 
                if stack and stack[-1] == connections_map[i]: 
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                
        if stack: 
            return False
        else:
            return True
        
        
        """
        :type s: str
        :rtype: bool
        """
        
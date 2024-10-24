class Solution(object):
    def isValid(self, s):
        
        stack = []
        map = {')' : '(', '}' : '{', ']': '['}
        
        for i in s: 
            if i in map:
                if stack and stack[-1] == map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack 
                
            
                
        """
        :type s: str
        :rtype: bool
        """
        
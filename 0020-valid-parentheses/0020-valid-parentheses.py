class Solution(object):
    def isValid(self, s):
        stack = []
        dictionary = { "}" : "{", ")" : "(", "]" : "[" }
        
        for i in s: 
            if i in dictionary:
                if stack and stack[-1] == dictionary[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        if not stack:
            return True
        else:
            return False
        
        """
        :type s: str
        :rtype: bool
        """
        
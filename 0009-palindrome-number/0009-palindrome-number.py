class Solution(object):
    def isPalindrome(self, x):
        bruh = str(x)
        left_ptr = 0 
        right_ptr = len(bruh) - 1 
        while left_ptr < right_ptr: 
            if bruh[left_ptr] == bruh[right_ptr]: 
                left_ptr = left_ptr + 1
                right_ptr = right_ptr -1 
            else:
                return False
        return True

                
        """
        :type x: int
        :rtype: bool
        """
        
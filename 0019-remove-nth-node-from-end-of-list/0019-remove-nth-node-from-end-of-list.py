# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0,head)
        lptr = dummy
        right = head
        while n > 0 and right: 
            right = right.next
            n = n - 1 
        while right: 
            lptr = lptr.next
            right = right.next
        lptr.next = lptr.next.next
        return dummy.next
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        
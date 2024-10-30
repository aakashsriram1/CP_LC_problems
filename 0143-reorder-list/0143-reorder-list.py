# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        # find the middle
        slow, fast = head, head 
        while fast.next and fast.next.next: 
            slow = slow.next 
            fast = fast.next.next 
        #reverse second half 
        prev, curr = None, slow.next 
        while curr: 
            next_temp = curr.next 
            curr.next = prev 
            prev = curr
            curr = next_temp 
        slow.next = None 
        #merge two halves 
        first, second = head, prev 
        while second: 
            tmp1, tmp2 = first.next,second.next 
            first.next = second
            second.next = tmp1
            first,second = tmp1,tmp2
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
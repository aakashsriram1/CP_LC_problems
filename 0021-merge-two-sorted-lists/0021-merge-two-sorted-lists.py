# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummyNode = rlist = ListNode()
        
        while list1 and list2: 
            if list1.val < list2.val: 
                rlist.next = list1
                list1 = list1.next 
            else: 
                rlist.next = list2
                list2 = list2.next 
            rlist = rlist.next
        if list1: 
            rlist.next = list1 
        else:
            rlist.next = list2
        return dummyNode.next
        
        
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
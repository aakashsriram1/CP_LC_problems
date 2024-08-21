# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()  # Dummy node to start the merged list
        rlist = dummy  # Pointer to build the new list
        
        while list1 and list2:  # Traverse both lists until one is exhausted
            if list1.val >= list2.val: 
                rlist.next = list2  # Attach the smaller node (list2)
                list2 = list2.next  # Move to the next node in list2
            else: 
                rlist.next = list1  # Attach the smaller node (list1)
                list1 = list1.next  # Move to the next node in list1
            rlist = rlist.next  # Move the pointer forward to the last node added
        
        # Attach the remaining nodes, if any
        if list1: 
            rlist.next = list1
        else:
            rlist.next = list2 
        
        return dummy.next  # Return the merged list starting after the dummy node
        
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

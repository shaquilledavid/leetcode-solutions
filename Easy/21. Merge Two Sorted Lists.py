"""
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1: 
            return list2
        
        if not list2:
            return list1

        #assign the start of the new sorted list
        if list1.val < list2.val:
            start = ListNode(list1.val)
            list1=list1.next
        else:
            start = ListNode(list2.val)
            list2=list2.next
            
        temp = start
        while list1:
            #if theres nothing to compare(list2 runs out): just append rest of list1 to start
            if not list2:
                temp.next = list1
                break
            
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            
            temp = temp.next
        
        if list2:
            temp.next = list2
        
        return start

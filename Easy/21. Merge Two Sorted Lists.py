"""
https://leetcode.com/problems/merge-two-sorted-lists/
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
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

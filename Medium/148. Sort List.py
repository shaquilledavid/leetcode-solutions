"""
https://leetcode.com/problems/sort-list/
Given the head of a linked list, return the list after sorting it in ascending
order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #make a copy of the linked list head
        #make a pointer to just the head
        if head == None:
            return None
        
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        
        vals.sort()
        new = ListNode(vals[0])
        temp = new
        i = 1
        while i < len(vals):
            new.next = ListNode(vals[i])
            new = new.next
            i += 1
        
        return temp

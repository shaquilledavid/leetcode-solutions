"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Given the head of a sorted linked list, delete all duplicates such that each
element appears only once. Return the linked list sorted as well.

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""

def deleteDuplicates(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return head
    
    temp = head.next
    prev = head
    while temp:
        if temp.val == prev.val:
            temp = temp.next
            prev.next = temp
        else:
            prev = temp
            temp = temp.next

    return head

"""
https://leetcode.com/problems/middle-of-the-linked-list/

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
"""

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    if head.next == None:
        return head
    
    temp = head
    
    length = 0
    while head:
        length += 1
        head = head.next

    midpoint = (length // 2) + 1

    iterations = 1
    while iterations < midpoint + 1:
        if iterations == midpoint:
            return temp
        else:
            iterations += 1
            temp = temp.next
            
    
    
    

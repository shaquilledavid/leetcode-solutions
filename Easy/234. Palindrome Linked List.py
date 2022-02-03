"""
https://leetcode.com/problems/palindrome-linked-list/
Given the head of a singly linked list, return true if it is a palindrome.

Input: head = [1,2,2,1]
Output: true
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """

    values = []
    while head:
        values.append(head.val)
        head = head.next

    
    reverse = []
    i = len(values) - 1

    while i > -1:
        reverse.append(values[i])
        i -= 1
        
    return values == reverse

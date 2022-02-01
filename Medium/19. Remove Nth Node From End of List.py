"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []
"""

class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """

    #base case where only one node.
    if head.next == None:
        if n == 1:
            return None

    #make a copy of the linked list we're given
    copy = head
    top = copy

    #in this step, we want to count how many nodes are in the linked list
    #so while head isn't none, we increase the counter and move on to next node
    length = 0
    while head:
        head = head.next #note that this is shortening head, which is why we made copies of head above.
        length += 1

    #iterations will store how many iterations we need to complete before we get to the node we need to remove
    iterations = length - n - 1 

    #basically, if iterations == -1, we know we must remove the first node. in this case we just return the head node's next
    if iterations == -1:
        copy = copy.next
        return copy 

    #traverse through the list. if we reach the number of iterations, we are at the node before the one to be removed
    start = 0
    while start < iterations + 1:
        if start == iterations:
            delink = copy.next.next     #the node we must delink is the one after to be removed
            copy.next = delink          #make the next node the one after the one to be removed (essentially, overwrite the node to be removed)
        else:
            copy = copy.next        #move forward a node if we are not at the node we need to remove
    
        start += 1

    return top          #we return top because top still points to the top of the head copy. in our traversal, copy points to next nodes .



head = ListNode(1)
head.next = ListNode(2)
#head.next.next = ListNode(3)
#head.next.next.next = ListNode(4)
#head.next.next.next.next = ListNode(5)

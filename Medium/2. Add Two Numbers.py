"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a
single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    carry = False
    temp = l1
    if l1.val + l2.val >= 10:
        l1.val = int(str(l1.val + l2.val)[1])
        carry = True
    else:
        l1.val = (l1.val + l2.val)
            
    l2 = l2.next
        
    while l2:
        if temp.next != None:
            temp = temp.next
            value = temp.val + l2.val
            if carry:
                value += 1
                carry = False
                
            if value >= 10:
                value = int(str(value)[1])
                carry = True
                    
            temp.val = value
            l2 = l2.next
            
        else:
            value = l2.val
            if carry:
                value += 1
                carry = False
            
                if value >= 10:
                    value = int(str(value)[1])
                    temp.next = ListNode(value)
                    carry = True
                else:
                    temp.next = ListNode(value)
                    temp = temp.next
                    l2=l2.next
            else:
                carry = False
                temp.next = ListNode(l2.val)
                temp=temp.next
                l2=l2.next

            
    if temp.next:
        temp = temp.next
        while temp:
            if carry:
                temp.val += 1
                carry = False
                if temp.val >= 10:
                    temp.val = int(str(temp.val)[1])
                    carry = True                    
                if temp.next:
                    temp = temp.next
                else:
                    break
                    
            else:
                temp = temp.next
    
    if carry:
        temp.next = ListNode(1)
        
    return l1
            

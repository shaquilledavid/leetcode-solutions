"""
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1
"""

def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    #brute force approach 
    #1st need to split up the digits, then need to square them, add them, update current number, repeat until we get 1

    #make a list, add the string representation of the digits to it, for digit in list, square, add, update
    current = n
    i = 0

    while i < 1000:
        if current == 1:
            return True
            
        stringrep = str(current)
        temp = 0
        for digit in stringrep:
            temp += int(digit)**2
        
        current = temp
        i += 1
            
    return False

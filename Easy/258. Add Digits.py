"""
https://leetcode.com/problems/add-digits/
Given an integer num, repeatedly add all its digits until the result has only
one digit, and return it.

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
"""

def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    #while the length of the number > 1
    #num = sum of the digits
    if num in range(0,10):
        return num

    while len(str(num)) > 1:
        numlist = [int(digit) for digit in str(num)]
        num = sum(numlist)
            
    return num

"""
https://leetcode.com/problems/add-binary/
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    carry = 0
    if len(a) < len(b):
        shorter = a 
        longer = b
    else:
        shorter = b
        longer = a
    
    difference = abs(len(a)-len(b))
    shorter = '0'*difference + shorter
    
    output = []
    i = len(longer) - 1
    
    while i > -1:
        if carry == 1:
            value = int(longer[i]) + int(shorter[i]) + carry
            if value == 1:
                output.append("1")
                carry = 0
            elif value == 2:
                output.append("0")
                carry = 1
            elif value == 3:
                output.append("1")
                carry = 1
        else:
            value = int(longer[i]) + int(shorter[i])
            if value == 0:
                output.append("0")
            elif value == 1:
                output.append("1")
            elif value == 2:
                output.append("0")
                carry = 1
        
        i -= 1
    
    if carry == 1:
        output.append("1")
        
    output.reverse()
    return ''.join(output)

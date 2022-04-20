"""
https://leetcode.com/problems/hamming-distance/
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.


Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
 

Constraints:

0 <= x, y <= 231 - 1
"""

def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    binrep_x = bin(x)[2:]
    binrep_y = bin(y)[2:]
    
    if len(binrep_x) > len(binrep_y):
        longer = binrep_x
        shorter = ('0'*(len(binrep_x) - len(binrep_y))) + binrep_y
    else:
        longer = binrep_y
        shorter = ('0'*(len(binrep_y) - len(binrep_x))) + binrep_x
    
    
    count = 0
    i = 0
    while i < len(longer):
        if longer[i] != shorter[i]:
            count += 1
        i += 1
    
    return count

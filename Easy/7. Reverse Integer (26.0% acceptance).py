"""
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        lst = []
        stringrep = str(x)
        
        for i in stringrep:
            lst.append(i)
            
        lst.reverse()
        
        reversedstr = ''.join(lst)
        
        if reversedstr[-1] == '-':
            final = -int(reversedstr[:-1])
        
        else:
            final = int(reversedstr)
            
        
        if final < -2**31 or final > 2**31 - 1:
            return 0
        
        return final

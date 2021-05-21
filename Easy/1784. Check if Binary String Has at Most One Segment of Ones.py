"""
https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

Given a binary string s ​​​​​without leading zeros, return true​​​ if s contains at most
one contiguous segment of ones. Otherwise, return false.

Example 1:

Input: s = "1001"
Output: false
Explanation: The ones do not form a contiguous segment.
Example 2:

Input: s = "110"
Output: true
"""

class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        
        #constraints gives us that s[0] = '1' always
        
        #put into a list
        lst = [i for i in s]
        index = 0
        
        #find the first 0
        while index < len(lst):
            if lst[index] == '1':
                index = index + 1
            else:
                break
        
        remaining = lst[index:]
        if '1' in remaining:
            return False
        
        return True
        

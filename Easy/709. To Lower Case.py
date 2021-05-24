"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3754/

Given a string s, return the string after replacing every uppercase letter with
the same lowercase letter. 

Example 1:

Input: s = "Hello"
Output: "hello"
Example 2:

Input: s = "here"
Output: "here"
Example 3:

Input: s = "LOVELY"
Output: "lovely"

### of course it's easy to use str.lower() to complete this, but we will attempt
this problem using ASCII relations ###
"""

class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        asc = []
        for i in s:
            asc.append(ord(i))
        
        lower = ''
        index = 0
        while index < len(asc):
            if asc[index] <= 90 and asc[index] >= 65:
                lower += chr(asc[index] + 32)
            else:
                lower += chr(asc[index])
            index = index + 1
        
        return lower

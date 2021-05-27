"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ss = []
        tt = []
        for i in s:
            ss.append(i)
        
        for j in t:
            tt.append(j)
            
        ss.sort()
        tt.sort()
        
        return ss == tt

"""
https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
"""

def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if s == "":
        return True
        
    #brute force way -> finding index[0] of substring in big string and then move on to index 1 and see if it occurs
    i = 0
    j = 0
    while j < len(t):
        if t[j] == s[i]:
            i += 1
            j += 1
            if i == len(s):
                return True
        else:
            j += 1
                
    return False

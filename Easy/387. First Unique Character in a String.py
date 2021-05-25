"""
https://leetcode.com/problems/first-unique-character-in-a-string/

Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        while i < len(s):
            if s[i] not in s[i+1:] and s[i] not in s[:i]:
                return i
            else:
                i += 1

        return -1

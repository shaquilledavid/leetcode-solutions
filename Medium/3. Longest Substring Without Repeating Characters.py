"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating
characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a
substring.
"""
from collections import deque

def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    queue = deque()
    L = 0 
    R = 0
    length = 0
    
    while R < len(s):
        
        if s[R] in queue:
            curr_length = len(s[L:R])
            if curr_length > length:
                length = curr_length
            
            queue.popleft()
            L += 1
            
        else:
            queue.append(s[R])
            R += 1
            if R == len(s):
                if len(s[L:R]) > length:
                    length = len(s[L:R])
    
    
    return length

"""
https://leetcode.com/problems/word-pattern/

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""

def wordPattern(pattern, s):
    """
    :type pattern: str
    :type s: str
    :rtype: bool
    """ 
    p = [letter for letter in pattern]
    words = s.split()

    if len(p) != len(words):
        return False

    match = {}

    i = 0
    while i < len(words):
        if p[i] in match:
            if match[p[i]] == words[i]:
                i += 1
            else:
                return False
        else:
            if words[i] not in match.values():
                match[p[i]] = words[i]
                i += 1
            else:
                return False

    return True
    

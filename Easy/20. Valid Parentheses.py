"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'
"""

def isValid(s: str) -> bool:
    opened = ['(', '[', '{']
    running = []
    validity = {')': '(', '}': '{', ']': '['}

    i = 0

    while i < len(s):
        if s[i] in opened:
            running.append(s[i])
            i += 1
            print(running)
        else:
            try:
                if validity[s[i]] == running[-1]:
                    x = running.pop()
                    i += 1
                else:
                    return False
            except:
                return False

    return len(running) == 0


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False

        opened = '' 

        pairs = {')': '(', ']': '[', '}': '{'}
        openBrackets = ['(', '[', '{']

        #iterate through the string

        for char in s:
            if char in openBrackets:
                opened+=char
            else:
                #if last index of opened is the matching bracket to what we are on now, remove from opened, and move on
                if len(opened) >= 1 and opened[-1] == pairs[char]:
                    opened = opened[:-1]
                else:
                    return False
        
        return opened == ''

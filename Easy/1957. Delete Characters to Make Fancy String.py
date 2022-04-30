"""
https://leetcode.com/problems/delete-characters-to-make-fancy-string/
A fancy string is a string where no three consecutive characters are equal.

Given a string s, delete the minimum possible number of characters from s to
make it fancy.

Return the final string after the deletion. It can be shown that the answer
will always be unique.

 
Example 1:

Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".
Example 2:

Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".
Example 3:
"""
def makeFancyString(self, s):
    """
    :type s: str
    :rtype: str
    """
    if len(s) < 3:
        return s
    
    i = 0 
    sequence = 0 
    letter = s[0]
    new_s = ''
    
    while i < len(s):
        if s[i] == letter:
            if sequence == 2:
                new_s += ''
            else:
                new_s += s[i]
                sequence += 1
        
        else:
            new_s += s[i]
            letter = s[i]
            sequence = 1
        
        i += 1
    
    return new_s

    """
    if len(s) < 3:
            return s
        
    i = 0 
    sequence = 0
    prev_char = ''
    new_s = ''
    
    for char in s:
        if char == prev_char:
            if sequence < 2:
                new_s += char
                sequence += 1
        
        else:
            prev_char = char
            sequence = 1
            new_s += char
    
    return new_s
    """

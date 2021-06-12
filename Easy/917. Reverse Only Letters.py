"""
https://leetcode.com/problems/reverse-only-letters/
Given a string s, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.


Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
"""

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = []
        indexes = []
        
        
        i = 0
        while i < len(s):
            if s[i].isalpha():
                letters.append(s[i])

            else:    
                indexes.append(i)

            i += 1
            
        letters.reverse()
        i = 0
        while i < len(indexes):
            letters.insert(indexes[i], s[indexes[i]])
            i += 1
        
        return ''.join(letters)

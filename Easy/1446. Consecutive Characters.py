"""
https://leetcode.com/problems/consecutive-characters/

Given a string s, the power of the string is the maximum length of a non-empty
substring that contains only one unique character.

Return the power of the string.

 

Example 1:

Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.
Example 2:

Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
Example 3:

Input: s = "triplepillooooow"
Output: 5
Example 4:

Input: s = "hooraaaaaaaaaaay"
Output: 11
Example 5:

Input: s = "tourist"
Output: 1
"""

class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or s == ' ':
            return 0
        
        power = 1
        count = 1
        i = 0
        
        
        while i < len(s)-1:
            
            if s[i] == s[i+1]:
                count += 1
                if count > power:
                    power = count
                i += 1
            
            else:
                count = 1
                i += 1
        
        return power

    

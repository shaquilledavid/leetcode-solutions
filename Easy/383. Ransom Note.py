"""
https://leetcode.com/problems/ransom-note/

Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.


Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        letters = [letter for letter in magazine]
        
        i = 0
        while i < len(ransomNote):
            if ransomNote[i] in letters:
                letters.remove(ransomNote[i])
                i = i + 1
            else:
                return False
        
        return True

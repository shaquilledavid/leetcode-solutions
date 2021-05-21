"""
https://leetcode.com/problems/check-if-the-sentence-is-pangram/

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
"""

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence) < 26:
            return False
        
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        
        lst = []
        
        for i in alpha:
            lst.append(i in sentence)
            
        if False in lst:
            return False
            
        return True

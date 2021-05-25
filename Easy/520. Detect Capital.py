"""
https://leetcode.com/problems/detect-capital/

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.


Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false
"""
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word[0].isupper():
            if word[1:].isupper():
                return True
            elif word[1:].islower():
                return True
            elif word[1:] == '':
                return True
            else:
                return False
        
        elif word.islower():
            return True
        
        else:
            return False


### a cleaner approach
"""
def detectCapitalUse(self, word):
        
        :type word: str
        :rtype: bool
        
        i = 1
        
        if word.isupper():
            return True
        if word.islower():
            return True
        elif word[0].isupper:
            while i < len(word):
                if word[i].islower():
                    i = i+1
                else:
                    return False
            return True
"""

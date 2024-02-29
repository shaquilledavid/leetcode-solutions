"""
https://leetcode.com/problems/length-of-last-word/

Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s == ' ':
            return 0
        
        else:
            lst = s.split()
            if len(lst) > 0:
                return len(lst[-1])
            else:
                return 0


        
def lengthOfLastWord2(self, s):
    """
    :type s: str
    :rtype: int
    """
    #base case
    if len(s) == 0:
        return 0

    #traversing the string from the back
    index = len(s) - 1
    lengthOfLastWord = 0

    #while traversing string backwards
    while index > -1:
        #use case 1: we encounter a char right away -> +1 to length and move to next char
            #we encounter another space, then break and return length
        if s[index].isalpha():
            lengthOfLastWord += 1
            if s[index-1] == ' ' or index == 0:
                break
            index -= 1

        #use case 2: we encounter a space
            #traverse backwards until the first letter, then begin count
            #in event that we have no characters, return 0 
        elif s[index] == ' ':
            index -= 1
            
    return lengthOfLastWord

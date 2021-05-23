"""
https://leetcode.com/problems/valid-palindrome/

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        
        lst = []
        lst2 = []
        if s == '':
            return True
        if len(s) == 1:
            return True
    
        for i in s:
            lst.append(i)

        #reverse the string
        reverseStr = s[::-1]
        for i in reverseStr:
            lst2.append(i)
        
        lst = deletePunctuation(lst)
        lst2 = deletePunctuation(lst2)
        
        if lst == lst2:
            return True
        else:
            return False

        
def deletePunctuation(lst):
    l = []
    i = 0
    while i < len(lst):
        if lst[i].isalnum() == True:
            l.append(lst[i])
        i = i + 1
    
    return l

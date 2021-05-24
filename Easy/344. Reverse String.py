import pdb

"""
Write a function that reverses a string. The input string is given as an array
of characters s.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
 

Follow up: Do not allocate extra space for another array. You must do this by
modifying the input array in-place with O(1) extra memory
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        jj = len(s)- 1

        if len(s)%2 == 0:
            while i != jj - 1:
                first = s[i]
                snd = s[jj]
                s[i] = snd
                s[jj] = first
                i += 1
                jj -= 1
            last = s[i]
            lass = s[jj]
            s[i] = lass
            s[jj] = last
        else:
            while i != jj:
                first = s[i]
                snd = s[jj]
                s[i] = snd
                s[jj] = first
                i += 1
                jj -= 1


        
            
s = ["H","a","n","n","a","h"]
k = ['h', 'e', 'l', 'l', 'o']
pdb.set_trace()
reverseString(s)
reverseString(k)

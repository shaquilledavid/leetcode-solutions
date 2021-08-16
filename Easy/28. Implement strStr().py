"""
https://leetcode.com/problems/implement-strstr/

28. Implement strStr()

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
"""

def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        
        if needle not in haystack:
            return -1
        
        else:
            lst = []
            for i in haystack:
                lst.append(i)
                
            j = 0
            while j < len(haystack):
                if lst[j] == needle[0]:
                    if ''.join(lst[j:j+len(needle)]) == needle:
                        return j
                    else:
                        j += 1
                else:
                    j += 1
        return -1

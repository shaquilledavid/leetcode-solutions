"""
https://leetcode.com/problems/find-all-anagrams-in-a-string/

Given two strings s and p, return an array of all the start indices of p's
anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    i = 0
    length = len(p)
    indices = []
    

    while i < len(s):
        if isAnagram(s[i: i + length], p):
            indices.append(i)
        i += 1

    return indices
            

def isAnagram(word1, word2):
    dee = {}
    deetwo = {}
    for letter in word1:
        if letter in dee:
            dee[letter] += 1
        else:
            dee[letter] = 0
    
    for l in word2:
        if l in deetwo:
            deetwo[l] += 1
        else:
            deetwo[l] = 0
    
    return dee == deetwo

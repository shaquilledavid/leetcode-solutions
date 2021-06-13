"""
https://leetcode.com/explore/challenge/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3777/
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the
concatenation of the two words words[i] + words[j] is a palindrome.


Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
"""
import pdb

def palindromePairs(words):
    """
    :type words: List[str]
    :rtype: List[List[int]]
    """
    lst = []
    i = 0
    j = 0
    while i < len(words):
        while j <= len(words)-1:
            if j == i:
                j += 1
            else:
                if isPalindrome(words[i] + words[j]):
                    lst.append([i, j])
                j += 1
        i += 1
        j = 0

    return lst

def isPalindrome(word):
    l = []
    for letter in word:
        l.append(letter)

    l.reverse()
    return ''.join(l) == word

    
words = ["abcd","dcba","lls","s","sssll"]
pdb.set_trace()
(palindromePairs(words))

"""
In an alien language, surprisingly they also use english lowercase letters, but
possibly in a different order. The order of the alphabet is some permutation of
lowercase letters.

Given a sequence of words written in the alien language, and the order of the
alphabet, return true if and only if the given words are sorted lexicographicaly
in this alien language.

 
Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
"""

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        #base case
        if len(words) == 1:
            return true
        
        if len(words) == 2:
            return compare2words(words[0], words[1], order)
        
        else:
            lst = []
            i = 0
            j = 1
            while j < len(words):
                lst.append(compare2words(words[i], words[j], order))
                i = i + 1
                j = j + 1
            
            if False in lst:
                return False
            else: 
                return True
        
def compare2words(w1, w2, order):
    if w1 == w2:
        return True
    
    if len(w1) > len(w2):
        x = len(w2) 
        if w2 == w1[0:x]: #check if w2 is entirely a substring of w1
            return False
        else:
            i = 0 
        while i < len(order):
            if order.index(w1[i]) < order.index(w2[i]):
                return True
            elif order.index(w1[i]) > order.index(w2[i]):
                return False
            elif order.index(w1[i]) == order.index(w2[i]):
                i = i + 1
    
    
    elif len(w1) <= len(w2):
        x = len(w1) 
        if w1 == w2[0:x]: #check if w2 is entirely a substring of w1
            return True
        
        i = 0 
        while i < len(order):
            if order.index(w1[i]) < order.index(w2[i]):
                return True
            elif order.index(w1[i]) > order.index(w2[i]):
                return False
            elif order.index(w1[i]) == order.index(w2[i]):
                i = i + 1

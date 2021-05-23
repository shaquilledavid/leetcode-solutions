"""

Given a string s, sort it in decreasing order based on the frequency of characters, and return the sorted string.

 

Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
class Solution:
    def frequencySort(self, s: str) -> str:

        d = {}

        #populate the dictionary
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        #update the dictionary, sorted by insertion order
        #https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
        updated = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

        #make a list so we can easily access the letters and their frequencies
        lst = []
        for item in updated.items():
            lst.append(item)
        lst.reverse()

        #format the return string
        s = ''
        for letter in lst:
            s += letter[0]*letter[1]

        return s
    

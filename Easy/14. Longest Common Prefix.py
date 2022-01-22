"""
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of
strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""


def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        
        i = 0
        common = numberCommonPrefix(strs[i], strs[i+1])
        i+=1 
        
        while i < len(strs)-1:
            if strs[i][0] != strs[i+1][0]:
                i += 1
            
            else:
                pre = numberCommonPrefix(strs[i], strs[i+1])
                if pre < common:
                    common = pre
                
                i += 1
        
        return strs[0][:common]
                    
             
            
def numberCommonPrefix(word1, word2):
    j = 0
    matches = 0
    
    if len(word1) < len(word2):
        shorter = word1
        longer = word2
    else:
        shorter = word2
        longer = word1
        
    while j < len(shorter):
        if shorter[j] == longer[j]:
            matches += 1
            j += 1
        else:
            break
    
    return matches

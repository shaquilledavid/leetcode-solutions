"""
https://leetcode.com/problems/partition-labels/
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.
 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
"""

def partitionLabels(self, s):
    """
    :type s: str
    :rtype: List[int]
    """
    parts = []
    copystr = s[::-1]
    length = 0
    start = 0
    i = 0
    
    while i < len(s):
        if s[i] in s[i+1:]:
            #find the last occurence of it
            indices = []
            index = len(s) - copystr.index(s[i])
            indices.append(index)
            i = index
            length = index - start
            
            temp = start
            while temp < index:
                if s[temp] in s[index:]:
                    indices.append(len(s) - copystr.index(s[temp]))
                    index = len(s) - copystr.index(s[temp])
                
                temp += 1

            parts.append(max(indices) - start)
            i = max(indices)
            start = i
            length = 0
        
        else:
            if start == i:
                parts.append(1)
                start += 1
                i += 1
            else:
                i+=1
            
            
    return parts
    

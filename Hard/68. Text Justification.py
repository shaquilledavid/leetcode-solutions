import math

"""
https://leetcode.com/problems/text-justification/

Given an array of strings words and a width maxWidth, format the text such that
each line has exactly maxWidth characters and is fully (left and right)
justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has
exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the
number of spaces on a line does not divide evenly between words, the empty slots
on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified and no extra space is
inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.
"""

def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    #determine how many lines we will need
    characters = 0
    for word in words:
        for ch in word:
            characters += 1
        characters += 1

    characters = characters - 1
    lines = math.ceil(characters/maxWidth)

    #our output of lines
    output = []

    
    i = 0
    chars = 0
    line = ''
    while i < len(words):
        if len(line) + len(words[i]) + 1 <= maxWidth:
            line += words[i] + ' '
            i += 1
        else:
            line = line[:-1] #takes out the space at the end
            lineWords = line.split()
            spaces = maxWidth - len(line.replace(' ', ''))
            
            #if we can distribute the spaces evenly
            if spaces % 2 == 0:
                evenly = int(spaces / (len(lineWords) - 1))
                justifiedLine = ''
                index = 0
                while index < len(lineWords):
                    if index == len(lineWords) - 1:
                        justifiedLine += lineWords[index]
                    else:
                        justifiedLine += lineWords[index] + (' ' * evenly)
                    index += 1
                    
                output.append(justifiedLine)

            else:
                output.append(line)
                
            #move on to the next line    
            line = words[i] + ' '
            i += 1

    #handles the left justification for the last line
    spaces = maxWidth - len(line)
    output.append(line + (' ' * spaces))
    
    return output
        
words = ["This", "is", "an", "example", "of", "text", "justification."]

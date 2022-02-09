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
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last
line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.
"""

def fullJustify(words, maxWidth):
    """
    :type words: List[str]
    :type maxWidth: int
    :rtype: List[str]
    """
    #our output of lines
    output = []

    
    i = 0
    chars = 0
    line = ''
    while i < len(words):
        if len(line) + len(words[i]) <= maxWidth:
            line += words[i] + ' '
            i += 1
        else:
            line = line[:-1] #takes out the space at the end
            lineWords = line.split()
            spaces = maxWidth - len(line.replace(' ', ''))  # characters left to fill
            
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

            #deal with the case of non even space distribution
            else:
                justifiedLine = ''
                #i know how many spaces i need. I know how many words i have...
                index = 0
                numberOfSpaces = len(lineWords) - 1  #this represents the number of spaces in the line.. as in there are 2 spaces between 3 words
                while index < len(lineWords):       
                    if index == len(lineWords) - 1:         #if we are on the last word, just add the word to the line. no need for spaces
                        justifiedLine += lineWords[index]   
                    else:
                        justifiedLine += lineWords[index] + (' ' * math.ceil(spaces/numberOfSpaces))    #add the word to the line AND the ceiling value of characters/number of spaces. (if there are 9 characters between 2 words, then we need 5 whitespaces (more first). then 4
                        spaces -= math.ceil(spaces/numberOfSpaces)      #update the number of characters left to fill
                        numberOfSpaces -= 1

                    index += 1
                        
                output.append(justifiedLine)
                
            #move on to the next line    
            line = words[i] + ' '
            i += 1

    #handles the left justification for the last line
    spaces = maxWidth - len(line)
    output.append(line + (' ' * spaces))
    
    return output
        
words = ["This", "is", "an", "example", "of", "text", "justification."]

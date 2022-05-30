"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3757/

Given a string array words, return the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. If no such two words exist,
return 0.

Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.

"""

def maxProduct(words):
    """
    :type words: List[str]
    :rtype: int
    """
    current_product = 0
    max_product = 0
    
    i = 0
    
    while i < len(words):
        j = i + 1
        while j < len(words):
            if noCommonality(words[i], words[j]) == True:
                prod = len(words[i]) * len(words[j])
                if prod > max_product:
                    max_product = prod
            
            j += 1
        i += 1
    
    return max_product
    

def noCommonality(word1, word2):
    for letter in word1:
        if letter in word2:
            return False
    
    return True



#######################################################
### Double checking with a Bitwise Masking function ###
#######################################################
def maxProduct2(words):
    """
    :type words: List[str]
    :rtype: int
    """
    words = list(set(words))
    n = len(words)
    if n == 1:
        return 0
    max = 0
    dyn = []
    for i in range(n):
            #convert all words to there equivalent bit string
        dyn.append(getLetterCount(words[i]))
    for i in range(n):
        for j in range(i+1,n):
                # to compare bit string using bitwise and operation
            if ((dyn[i] & dyn[j])== 0) and (len(words[i]) * len(words[j])) > max:
                max = len(words[i]) * len(words[j])
    return max

def getLetterCount(word):
    result = 0
    
    for w in set(word):
        result |= 1 << (ord(w) - ord('a'))

    return result

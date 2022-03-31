"""
The count-and-say sequence is a sequence of digit strings defined by the
recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of
groups so that each group is a contiguous section all of the same character.
Then for each group, say the number of characters, then say the character.
To convert the saying into a digit string, replace the counts with a number
and concatenate every saying.

For example, the saying and conversion for digit string "3322251":
(2 3's, 3 2's, 1 5, and 1 1)
= "23321511"

Given a positive integer n, return the nth term of the count-and-say sequence.

Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:
Input: n = 4
Output: "1211"

Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

SUBMISSION RESUTLS:
Runtime: 24 ms, faster than 97.89% of Python online submissions for Count and Say.
Memory Usage: 13.4 MB, less than 84.68% of Python online submissions for Count and Say.
"""

def countAndSay(self, n):
    """
    :type n: int
    :rtype: str
    """
    if n == 1:
        return "1"
    
    sayings = ["1"] * n
    
    i = 1
    while i < len(sayings):
        sayings[i] = sayIt(sayings[i-1])
        i += 1
    #DFS approach
    return sayings[n-1]
            
        
def sayIt(number):
    #number is in string representation
    saying = ''
    i = 0
    digit = number[i]
    count = 0
    while i < len(number):
        if number[i] == digit: #if the number is the same as the digit, increase count
            count += 1
            i += 1
        else:
            saying += str(count) #add the count to the string, then the digit, then move on.
            saying += digit
            digit = number[i]
            count = 0
    
    saying += str(count) + str(digit)
    return saying
            

"""
https://leetcode.com/problems/self-dividing-numbers/

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0,
and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self
dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        lst = []
        for i in range(left, right+1):
            if isSelfDiv(i) == True:
                lst.append(i)
        
        return lst
            
        
def isSelfDiv(num):
    string = str(num)
    
    bools = []
    i = 0
    while i < len(string):
        
        if int(string[i]) == 0:
            return False
        
        elif num % int(string[i]) == 0:
            bools.append(True)
            i = i + 1
     
        else:
            return False
    
    
    return True

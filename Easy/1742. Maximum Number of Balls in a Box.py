"""
https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

You are working in a ball factory where you have n balls numbered from lowLimit
up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite
number of boxes numbered from 1 to infinity.

Your job at this factory is to put each ball in the box with a number equal to
the sum of digits of the ball's number. For example, the ball number 321 will
be put in the box number 3 + 2 + 1 = 6 and the ball number 10 will be put in
the box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of balls in the
box with the most balls.


Example 1:

Input: lowLimit = 1, highLimit = 10
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  2 1 1 1 1 1 1 1 1 0  0  ...
Box 1 has the most number of balls with 2 balls.
Example 2:

Input: lowLimit = 5, highLimit = 15
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
Boxes 5 and 6 have the most number of balls with 2 balls in each.
Example 3:

Input: lowLimit = 19, highLimit = 28
Output: 2
Explanation:
Box Number:  1 2 3 4 5 6 7 8 9 10 11 12 ...
Ball Count:  0 1 1 1 1 1 1 1 1 2  0  0  ...
Box 10 has the most number of balls with 2 balls.
"""
class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        # n == highLimit - lowLimit + 1 
        n = highLimit - lowLimit + 1
        
        #make a dictionary, to hold box numbers and balls
        d = {}
        for i in range(1, highLimit+1):
            d[str(i)] = 0
        
        #create the range of balls, starts with lowlimit to highlimit inclusive
        lst = []
        for i in range(lowLimit, highLimit + 1):
            lst.append(i)
            
        #populate dictionary
        for i in lst:
            if str(boxNumber(i)) in d:
                d[str(boxNumber(i))] += 1
        
        return max(d.values())

        
        
#make a function that takes a number and return its box number
def boxNumber(n):
    stringrep = str(n)
    
    count = 0
    for i in stringrep:
        count = count + int(i)
        
    return count

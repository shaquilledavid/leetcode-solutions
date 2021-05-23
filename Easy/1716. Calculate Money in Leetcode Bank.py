"""
https://leetcode.com/problems/calculate-money-in-leetcode-bank/

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

 

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.
Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.
Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
"""

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        
        total = 0
        day_before = 0
        previous_monday = 0
        
        i = 0
        while i < n:
            if i%7 == 0:  #monday case
                total = total + (1 + previous_monday)
                day_before = (1 + previous_monday)
                i = i + 1
                previous_monday = previous_monday + 1
            
            else:
                total = total + (day_before + 1)
                day_before += 1
                i = i + 1
        
        return total

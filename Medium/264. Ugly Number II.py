"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

 

Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
"""

        
def nthUglyNumber(n):
    """
    :type n: int
    :rtype: int
    """

    if n == 1:
        return 1
    
    uglies = []
    for i in range(1690):
        if i%2 == 0 or i%3 == 0 or i%5 == 0:
            uglies.append(i)

    return uglies[n-1]

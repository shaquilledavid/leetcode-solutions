"""
https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions
after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version
is bad. Implement a function to find the first bad version. You should minimize
the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    # we know for a fact that isBadVersion(n) == True?
    if n == 1:
        return 1
    
    i = 1
    nn=n
    half = (nn+i)//2
    while i != nn:
        half = (nn+i)//2
        if isBadVersion(half) == True:
            #then the first bad is in the range(i,half)
            nn = half
        else:
            #then the first bad is in the range(half, n)
            i = half + 1
            if i == nn:
                return i
    
    return half

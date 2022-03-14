"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

 
Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    #bottomUp 
    dp = [0]*(n+1)
    dp[0] = 1
    print(dp)
    
    i = 1
    while i < n+1:
        dp[i] += dp[i-2]
        dp[i] += dp[i-1]
        i += 1
    
    print(dp)
    return dp[n]

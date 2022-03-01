"""
https://leetcode.com/problems/counting-bits/submissions/
Given an integer n, return an array ans of length n + 1 such that for each i
(0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        #need a list of # of 1's in binary rep of each number range(0, n+1)
        ans = []
        
        for number in range(0, n+1):
            ans.append(countOnes(str(bin(number))))
        
        return ans
        

        
def countOnes(number):
    count = 0
    for i in number:
        if i == '1':
            count += 1
    return count

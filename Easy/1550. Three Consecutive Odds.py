"""
https://leetcode.com/problems/three-consecutive-odds/submissions/

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
"""

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        i = 0 
        count = 0
        
        while i < len(arr):
            if arr[i] % 2 != 0:
                count = count + 1
                if count == 3:
                    return True
                i = i + 1
            else:
                count = 0 
                i = i + 1
        
        return False

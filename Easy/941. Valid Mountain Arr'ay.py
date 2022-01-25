"""
https://leetcode.com/problems/valid-mountain-array/submissions/
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
"""

def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        if len(arr) < 3:
            return False
        
        if arr[0] > arr[1]:
            return False
        
        increasing = True
        i = 0
        changes = 0
        while i < len(arr) - 1:
            if changes > 1:
                return False
            
            if increasing == True:
                if arr[i] < arr[i+1]:
                    i += 1
                elif arr[i] > arr[i+1]:
                    increasing = False
                    i += 1
                    changes += 1
                else:
                    return False
            
            else:
                if arr[i] < arr[i+1]:
                    increasing = True
                    i += 1
                    changes += 1
                elif arr[i] > arr[i+1]:
                    i += 1
                else:
                    return False
                    
                
        return (increasing == False) and (changes == 1)

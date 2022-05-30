"""
Given an array of positive integers nums and a positive integer target, return
the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1,
numsr] of which the sum is greater than or equal to target. If there is no such
subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem
constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, try coding another
solution of which the time complexity is O(n log(n)).
"""

def minSubArrayLen(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    L = 0
    R = 0 
    
    if target in nums:
        return 1
    
    minLength = float('inf')
    currentLength = 1
    
    while L < len(nums):
        
        if len(nums[L:R+1]) > minLength:
            L+=1
            continue
        
        curr_sum = sum(nums[L:R+1])
        
        if sum(nums[L:R+1]) >= target:
            if currentLength < minLength:
                minLength = currentLength
            L += 1
            
        else:
            if R == len(nums) - 1:
                L += 1
                
            else:
                R += 1
            
        currentLength = len(nums[L:R+1])
            
    
    
    return 0 if minLength == float('inf') else minLength

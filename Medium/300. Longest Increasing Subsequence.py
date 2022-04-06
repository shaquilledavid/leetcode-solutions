"""
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting
some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #iterate over every number
    #check [number:], choose smallest bigger int
    # move index there, increment length
    maxlength = 1
    
    i = 0
    while i < len(nums):
        j = i
        current = nums[j]
        length = 1
        while j < len(nums):
            #if there is a number bigger than the current in nums[j+1:]
            #choose the min one
            if len(allBigger(current, nums[j+1:])) == 0:
                j += 1

            elif min(allBigger(current, nums[j+1:])) > current:
                current = min(allBigger(current, nums[j+1:]))
                j = j + nums[j:].index(current) #one issue here where itll go back if num is duplicate
                length += 1
                
            else:
                j += 1
        
        if length > maxlength:
            maxlength = length
        i += 1
            
    return maxlength 
    
    
    
def allBigger(num, arr):
    #return the array with numbers only bigger than num
    ret = []
    for number in arr:
        if number > num:
            ret.append(number)
    return ret


nums = [10,9,2,5,3,7,101,18]

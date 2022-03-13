"""
https://leetcode.com/problems/summary-ranges/submissions/

You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the
array exactly. That is, each element of nums is covered by exactly one of the
ranges, and there is no integer x such that x is in one of the ranges but not
in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
"""

def summaryRanges(nums):
    #iterate through the list,
    #case 1-> standalone range. 
    #case 2->proper range
    #capture when we're starting a new range. iterate through. when done, set capture start to current index
    
    if len(nums) == 0:
        return []
    
    if len(nums) == 1:
        return [str(nums[0])]
    
    output = []
    i = 0
    rangeList = []
    
    
    while i < len(nums):
        rangeList.append(nums[i])
        if i == len(nums) - 1:
            break
        
        elif nums[i+1] == nums[i] + 1:
            rangeList.append(nums[i+1])
            
        else:
            if len(rangeList) == 1:
                output.append(str(rangeList[0]))
                rangeList = []
                
            else:
                output.append(str(rangeList[0]) + "->" + str(rangeList[-1]))
                rangeList = []

        i += 1
            
    
    if len(rangeList) == 1:
        output.append(str(rangeList[0]))
    else:
        output.append(str(rangeList[0]) + "->" + str(rangeList[-1]))
            
    return output

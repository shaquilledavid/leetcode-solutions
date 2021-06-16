"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        i = 0
        
        while i < len(nums):
            if str(nums[i]) in d:
                d[str(nums[i])] += 1
            else:
                d[str(nums[i])] = 0
            i += 1
        
        vals = []
        keys = []
        
        for i in d.keys():
            keys.append(i)
            
        for j in d.values():
            vals.append(j)
            
        
        return int(keys[vals.index(max(vals))])


######## Terrible time complexity

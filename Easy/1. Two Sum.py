"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #make a hashmap of nums[i] and its index
        #iterate over nums, add the num:index into the hashmap
        #however, if we've already come across the number that'll reach target, return current index and composite index
        d = {}

        i = 0 
        while i < len(nums):
            composite = target - nums[i]
            if composite in d:
                return [i, d[composite]]
            
            else:
                d[nums[i]] = i
                i += 1

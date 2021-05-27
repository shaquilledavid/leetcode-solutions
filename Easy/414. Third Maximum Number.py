"""
https://leetcode.com/problems/third-maximum-number/

Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #we will use a set, since sets do not allow duplicate items

        numset = set()
        for i in nums:
            numset.add(i)

        lst = list(numset)
        lst.sort()

        if len(lst) >= 3:
            return lst[-3]
        else:
            return max(lst)

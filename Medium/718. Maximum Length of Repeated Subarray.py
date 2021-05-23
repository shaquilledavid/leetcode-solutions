"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
Given two integer arrays nums1 and nums2, return the maximum length of a subarray that appears in both arrays.
 

Example 1:

Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1].
Example 2:

Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5
"""
import pdb


def findLength(nums1, nums2):

    if nums1 == nums2:
        return len(nums1)

    i = 0
    maxLength = 0
    count = 0
    ii = 0

    if nums1 <= nums2:
        while i < len(nums1):
            if nums1[i] in nums2:
                ii = nums2.index(nums1[i])
                ii += count
                try:
                    if nums1[i+1] == nums2[ii+1]:
                        count += 1
                        if count > maxLength:
                            maxLength = count
                        i += 1
                    else:
                        count = 0
                        i += 1
                except:                    
                    break

            else:
                count = 0
                i += 1

        return maxLength + 1 

    else:
        while i < len(nums2):
            if nums2[i] in nums1:
                
                try:
                    if nums2[i+1] == nums1[nums1.index(nums2[i])+1]:
                        count += 1
                        if count > maxLength:
                            maxLength = count
                        i += 1
                    else:
                        count = 0
                        i += 1
                except:
                    break

            else:
                count = 0
                i += 1

        return maxLength + 1




nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
pdb.set_trace()
findLength(nums1, nums2)

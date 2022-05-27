"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
Given two sorted arrays nums1 and nums2 of size m and n respectively, return
the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

def sortArrays(nums1, nums2):
    #make pointers for each list, go into a while loop, compare the pointers, add accordingly, and update pointer
    #if at any point one list is empty, append other list and break
    
    i = 0  
    j = 0
    arr = []
    
    while i < len(nums1):
        if nums1[i] < nums2[j]:
            arr.append(nums1[i])
            i += 1
            if i == len(nums1):
                arr = arr + nums2[j:]
                break
        
        elif nums1[i] > nums2[j]:
            arr.append(nums2[j])
            j += 1
            if j == len(nums2):
                arr = arr + nums1[i:]
                break
        
        elif nums1[i] == nums2[j]:
            arr.append(nums1[i])
            arr.append(nums2[j])
            i += 1
            j += 1
    
    return arr

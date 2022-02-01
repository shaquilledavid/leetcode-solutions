"""
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """
    flowers_left = n
    
    #base case
    if len(flowerbed) == 1:
         if flowerbed[0] == 0:
            flowerbed[0] = 1
            flowers_left -= 1
            return flowers_left <= 0
        
    i = 0

    while i < len(flowerbed):
        if i == 0:
            if flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                flowers_left -= 1
            i += 1
            
        elif i == len(flowerbed) - 1:
            if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                flowers_left -= 1
            i+=1
            
        elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
            flowerbed[i] = 1
            flowers_left -= 1
            i += 1
        
        else:
            i += 1
            
    return flowers_left <= 0
            
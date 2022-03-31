"""
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value target in an m x n
integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous
row.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""
def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if len(matrix) == 1:
        return target in matrix[0]
    
    if target in matrix[-1]:
        return True
    
    start = 0
    nex = 1
    while nex < len(matrix):
        if target >= matrix[start][0] and target <= matrix[nex][0]:
            if target in matrix[start] or target in matrix[nex]:
                return True
            else:
                return False
            
        else:
            start += 1
            nex += 1
    
    return False

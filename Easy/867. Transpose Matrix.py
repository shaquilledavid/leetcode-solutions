"""
https://leetcode.com/problems/transpose-matrix/

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal,
switching the matrix's row and column indices.


Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
"""
def transpose(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    queue = deque()
    newRowLength = len(matrix[0])
    newColLength = len(matrix)
    
    r = 0
    c = 0 
    while c < len(matrix[0]):
        while r < len(matrix):
            queue.append(matrix[r][c])
            r += 1
        
        c += 1
        r = 0

    #the matrix isn't always guaranteed to be NxM, so we must account for the
    #possibilities where N!=M
    col = 0
    row = 0
    newMatrix = []
    
    while row < newRowLength:
        r = [] #make a new row as necessary. 
        while col < newColLength:
            r.append(queue.popleft())
            col += 1
        
        newMatrix.append(r)
        col = 0
        row += 1
        
        
    
    return newMatrix

"""
"""

def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])
    #what if we use a queue, we notice a pattern where LIFO could be useful ([1,2,3], [4,5,6], [7,8,9]) =  ([7,4,1], [8,5,2], [9,6,3])
    #if i traverse the matrix by position , my queue would look like [1,4,7,2,5,8,3,6,9]
    #since the queue is LIFO, we pop 9, and insert it into the first position of last row, then pop 6 into 2nd position of last row.... decrement the row and start over
    
    q = deque()
    
    #populate the queue
    col = 0 
    while col < n:
        i=0
        while i < n:
            q.append(matrix[i][col])
            i += 1
        
        col += 1
    
    #repopulate the matrix after popping from queue
    index = n - 1
    
    while index >= 0:
        col = 0
        while col < n:
            matrix[index][col] = q.pop()
            col += 1
        
        index -= 1
    
    
    return matrix 

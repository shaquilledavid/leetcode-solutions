"""
https://leetcode.com/problems/queens-that-can-attack-the-king/
On an 8x8 chessboard, there can be multiple Black Queens and one White King.

Given an array of integer coordinates queens that represents the positions of
the Black Queens, and a pair of coordinates king that represent the position of
the White King, return the coordinates of all the queens (in any order) that
can attack the King.


Example 1:

Input: queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
Output: [[0,1],[1,0],[3,3]]
Explanation:  
The queen at [0,1] can attack the king cause they're in the same row. 
The queen at [1,0] can attack the king cause they're in the same column. 
The queen at [3,3] can attack the king cause they're in the same diagnal. 
The queen at [0,4] can't attack the king cause it's blocked by the queen at[0,1]. 
The queen at [4,0] can't attack the king cause it's blocked by the queen at [1,0]. 
The queen at [2,4] can't attack the king cause it's not in the same row/column/diagnal as the king.

Example 2:
Input: queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
Output: [[2,2],[3,4],[4,4]]

Example 3:
Input: queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
Output: [[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]
"""

def queensAttacktheKing(queens, king):
    """
    :type queens: List[List[int]]
    :type king: List[int]
    :rtype: List[List[int]]
    """
    
    #initialize our grid, then populate
    grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
    for i in range(8):
        grid.append([0, 0, 0, 0, 0, 0, 0, 0])
        
    grid[king[0]][king[1]] = 'K'
    for queen in queens:
        grid[queen[0]][queen[1]] = 'Q'
    
    
    blackQueens = []

    #for all our queens, lets see if we can get to the king.
    #change our queen to a B. this is the one we are working with. after we traverse the grid, change it back to a Q
    for queen in queens:
        grid[queen[0]][queen[1]] = 'B'
        if helper(queen[0], queen[1], grid, king) == 1:
            blackQueens.append(queen) #add this queen to our result list if she can get to the king
        
        grid[queen[0]][queen[1]] = 'Q'
    
    return blackQueens

        
        
def helper(row, col, grid, king):
    #helper function that recursively calls if the queen is movable towards the king
    #if at any point the queen encouters the king, return 1. if the queen encounters another
    #queen blocking, return 0
    
    if grid[row][col] == 'K':
        return 1
        
    
    if grid[row][col] == 'Q':
        return 0
    
    #if we are on the same row as the king we only want to move left or right
    elif row == king[0]:
        if col < king[1]:
            return helper(row, col + 1, grid, king)
        else:
            return helper(row, col - 1, grid, king)
    
    
    #if we are on the same column as the king move up or down
    elif col == king[1]:
        if row < king[0]:
            return helper(row + 1, col, grid, king)
        else:
            return helper(row-1, col, grid, king)
    
    #if we are directly in a diagonal, we have 4 cases of movements
    elif abs(row - king[0]) == abs(col - king[1]):
        
        #case up left -> if the king's row < row and king col < col
        if king[0] < row and king[1] < col:
            return helper(row - 1, col - 1, grid, king)
        
        #upright -> if the kings row < row and king col > col
        elif king[0] < row and king[1] > col:
            return helper(row - 1, col + 1, grid, king)
        
        #downleft -> if the kings row > row and king col < col
        elif king[0] > row and king[1] < col:
            return helper(row + 1, col - 1, grid, king)
        
        #downright -> if the kings row > row and king col > col
        elif king[0] > row and king[1] > col:
            return helper(row + 1, col + 1, grid, king)
        
        else:
            return 0
    

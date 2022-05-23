"""
https://leetcode.com/problems/rotting-oranges/

You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""
from collections import deque

def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    minutes = 0
    twos = []
    freshOranges = 0

    #first step is to locate all the twos on our starting grid
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):
            if grid[i][j] == 2:
                twos.append([i, j])
            if grid[i][j] == 1:
                freshOranges += 1
            j += 1

        i += 1
    
    #next, we implement our queue to keep track of the points visited in our BFS traversal
    q = deque()
    directions = [[0,1], [1, 0], [-1, 0], [0, -1]]

    #do i add all initial twos to the queue, pop it, check for fresh oranges using directions then add to queue if needed?
    for two in twos:
        q.append(two)
        
    while q and freshOranges > 0:
        for rottenOrange in list(q):            #it needs to be list(q) or else q will be mutated during iteration and cause error https://stackoverflow.com/questions/30107212/add-to-a-deque-being-iterated-in-python
            #check directional movements now
            #scenarios for a rottenOrange: 1. it is on a boundary -> cant go up or cant go down or cant go left or cant go right
            #                              2. it has no boundary -> check all directions
            for direction in directions:
                adjacent = [rottenOrange[0] + direction[0], rottenOrange[1] + direction[1]]
                try:
                    if grid[adjacent[0]][adjacent[1]] == 1 and (adjacent[0] != -1 and adjacent[1] != -1):
                        grid[adjacent[0]][adjacent[1]] = 2
                        freshOranges -= 1
                        q.append(adjacent)

                except:
                    pass
            
        q.popleft()
        minutes += 1

    return minutes if freshOranges == 0 else -1 
                        
        
    
            

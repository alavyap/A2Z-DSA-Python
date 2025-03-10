'''
Link :> https://leetcode.com/problems/rotting-oranges/description/


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
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
'''
# Brute Force 
from collections import deque


def rottenOragnes(grid):
    
    rows = len(grid)
    cols = len(grid[0])
    total_time = 0
    
    
    while True :
        changed = False
        new_grid = [row[:] for row in grid]
        
        for i in range (rows):
            for j in range (cols):
                if grid[i][j] ==2 :
                    for x,y in [(i-1,j),(i + 1,j), (i,j-1),(i,j+1)]:
                        if 0 <= x < rows and 0 <=y < cols and grid[x][y] == 1 :
                            new_grid[x][y] = 2 
                            changed =True

        if not changed:
            break 
        
        grid = new_grid 
        total_time += 1 
        
    for row in grid :
        if 1 in row :
            return -1 
    return total_time


# Optimal Appraoch 

def orangeRottening(grid):
    rows,cols = len(grid), len(grid[0])
    queue = deque() 
    fresh = 0 
    
    
    for i in range(rows):
        for j in range (cols):
            if grid[i][j] == 2 :
                queue.append((i,j))
            elif grid[i][j] == 1 :
                fresh += 1 
                
                
    minutes = 0 
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    while queue and fresh > 0 :
        minutes += 1 
        
        for _ in range  (len(queue)):
            i,j = queue.popleft() 
            
            for dr,dc in directions :
                dr,dc =  i+ dr , j+dc
                
                if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] == 1 :
                    grid[dr][dc] = 2 
                    fresh -= 1 
                    
                    queue.append((dr,dc))     
                    
    return minutes if fresh == 0 else -1
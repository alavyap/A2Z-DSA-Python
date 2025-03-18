'''
Link :> https://leetcode.com/problems/number-of-enclaves/description/

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

Example 1:
Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.


Example 2:
Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
'''

from collections import deque


def numEnclaves(grid):
    
    m = len(grid)
    n = len(grid[0])
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    
    queue = deque()
    
    for i in range (m):
        for j in range (n):
            if (i == 0 or i == m-1 or j == 0 or j == n-1) and grid[i][j] == 1 :
               queue.append((i,j))
               grid[i][j] = -1
               
               
    while queue :
        x,y = queue.popleft() 
        
        for dx,dy in directions :
            nx,ny = x + dx, y +dy 
            if 0 <= nx and 0 <= ny < n and grid[nx][ny] == 1 :
                grid[nx][ny] =-1
                queue.append((nx,ny))
                
                
    count = 0 
    for i in range (m):
        for j in range(n):
             if grid[i][j] == 1 :
                count += 1 
    return count  
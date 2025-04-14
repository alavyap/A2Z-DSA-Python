'''
Link :> https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.


Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 
Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
'''



'''
if grid[0][0] ==1 or grid[n-1][n-1] ==1 return -1 
count = 0

'''
from collections import deque


def spinMaze(grid):
    
    n = len(grid)
    if grid[0][0] != 0 or grid[n-1][n-1] != 0: 
       return -1 
    
    directions = [
        (0,-1),(0,1),(1,0),(-1,0),
        (-1,-1),(1,1),(-1,1),(1,-1)
    ]
    
    queue = deque([(0,0,1)])  #[row,col,distance]
    
    vis = [[False] * n for _ in range (n)]
    vis[0][0] = True 
    
    while queue : 
        row,col,dist = queue.popleft() 
        
        if row == n-1 and col == n-1 :
            return dist 
        
        for dr,dc in directions : 
            newRow,newCol = row + dr, col + dc
            
            if 0 <= newRow < n and 0 <= newCol < n and grid[newRow][newCol] == 0  and not vis[newRow][newCol]: 
                vis[newRow][newCol] = True 
                queue.append(newRow,newCol,dist+1)
                
    return -1 
            
    
    
    
'''
Link :> https://leetcode.com/problems/01-matrix/


Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

 

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
'''

from collections import deque


def updatedMatrix(mat):
    
    n = len(mat)
    m = len(mat[0])
    
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    result = [[float("inf")] * m for _ in range(n)]
    queue = deque()
    
    for i in range (n):
        for j in range (m):
            if mat[i][j] == 0 :
                result[i][j] = 0 
                queue.append((i,j))
                
                
    while queue :
        x,y = queue.popleft() 
        for dx,dy in directions :
            nx,ny = x +dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m :
                
                if result[nx][ny] > result[x][y] + 1 :
                    result[nx][ny] = result[x][y] +1 
                    queue.append((nx,ny))
    return result
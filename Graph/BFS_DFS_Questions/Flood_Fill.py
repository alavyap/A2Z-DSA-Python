'''
Link :> https://leetcode.com/problems/flood-fill/description/

You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

 

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation:
The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], color < 216
0 <= sr < m
0 <= sc < n

'''

# Brute Force  > As we are doing the changes in the input which is wrong practice. //**DFS Approach**\\
from collections import deque


def floodFillBrute(image,sr,sc,color):
    original_color = image[sr][sc]
    
    if original_color == color: 
        return image 
    
    
    def dfs(r,c):
        
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color: 
            return 
        
        image [r][c] = color 
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
        
    dfs(sr,sc)
    return image 
    
    
# DFS Optimal Approach


def floodFillDFS(image,sr,sc,color):
    
    initialColor = image[sr][sc]
    
    if initialColor == color :
        return image 
    
    ans = [row[:] for row in image]
    
    delRow = [-1,0,1,0]
    delCol = [0,1,0,-1]
    
    def dfs(row,col):
        ans[row][col] = color
        
        for i in range (4):
            nrow = row + delRow[i] 
            ncol = col +delCol[i] 
            
            if 0 <= nrow < len(image) and 0 <= ncol < len(image[0]) and image[nrow][ncol] == initialColor and ans[nrow][ncol] != color :
                dfs(nrow,ncol)
                
    dfs(sr,sc)
    
    return ans


# Optimal Approach  >> BFS Approach 

def floodOptimalBFS(image,sr,sc,color):
    
    original_color = image[sr][sc]
    
    if original_color == color :
        return image 
    
    queue = deque()
    queue.append((sr,sc))   
    image[sr][sc] = color 
    
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    
    while queue :
        r,c = queue.popleft() 
        
        
        for dr,dc in directions :
            nr,nc = r + dr, c +dc 
            
            if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == original_color :
                image[nr][nc] = color 
                queue.append((nr,nc))
                
    return image
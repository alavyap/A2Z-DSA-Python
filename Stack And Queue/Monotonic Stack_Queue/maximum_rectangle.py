'''
LeetCode:> https://leetcode.com/problems/maximal-rectangle/description/

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
'''

# Better Approach 
from turtle import width


def maxiRect(matrix):
    
    if not matrix :
        return 0 
    
    matrix = [[int(x) for x in row ] for row in matrix]
    n = len(matrix)
    m = len(matrix[0])
    
    heights = [0] * m
    ans = 0
    
    for i in range (n):
        for j in range (m):
            
            if matrix[i][j] == 1 :
                heights[j] += 1 
            else :
                heights[j] = 0 
                
        ans = max(ans,maxin_histogram(heights))
    return ans 



def maxin_histogram(heights):
    stack = [] 
    max_area = 0 
    index = 0 
    
    
    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]] : 
            stack.append(index)
            index += 1 
        else : 
            top = stack.pop() 
            area = heights[top] * ((index -stack[-1] -1 ) if stack else index)
            max_area = max(max_area,area)
            
    
    while stack :
        top = stack.pop() 
        area = heights[top] * ((index - stack[-1] - 1 )  if stack else index ) 
        max_area = max(max_area,area)
        
    return max_area


# Optimal Approach 
def maximumArea (matrix): 
    if not matrix or not matrix[0] :
        return 0 
    
    rows,cols = len(matrix), len(matrix[0])
    
    heights = [0] * (cols + 1 )
    max_area = 0 
    
    for row in range (rows):
        stack = [-1] 
        
        for col in range  (cols + 1) :
            if col < cols : 
                if matrix[row][col] == "1" :
                    heights[col] += 1 
                else :
                    heights[col] = 0 
                    
            while stack[-1] != -1 and heights[col] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = col - stack[-1] -1 
                max_area = max(max_area, height * width)
                    
            stack.append(col)
                
    return max_area
 

a = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(maximumArea(a))
            
            
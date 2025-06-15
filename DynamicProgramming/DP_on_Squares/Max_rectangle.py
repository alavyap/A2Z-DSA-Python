'''
Link :> https://leetcode.com/problems/maximal-rectangle/

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


def maxArea(matrix): 
    
    if not matrix or not  matrix[0]:
        return 0 
    
    n = len(matrix)
    m = len(matrix[0])
    height = [0] * m
    maxArea = 0 
    
    
    for i in range (n): 
        for j in range (m): 
            if matrix[i][j] == "1": 
                height[j] += 1 
            else: 
                height[j] = 0 
                
        area = helper(height)
        maxArea = max(maxArea,area)
    return maxArea

def helper(histo):
    stack = [] 
    maxA = 0 
    n = len(histo)
    histo = histo + [0]  # Append a zero to flush out remaining heights
    
    for i in range(n + 1):
        while stack and histo[stack[-1]] > histo[i]:
            height = histo[stack.pop()]
            if not stack:
                width = i
            else:
                width = i - stack[-1] - 1
            maxA = max(maxA, width * height)
        stack.append(i)
        
    return maxA
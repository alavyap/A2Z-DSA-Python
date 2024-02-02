'''
Coding Ninja : > https://www.codingninjas.com/studio/problems/981260?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
LeetCode : > https://leetcode.com/problems/rotate-image/
Problem Statement : Given a matrix, your task is to rotate the matrix 90 degrees clockwise🔁
Example
Input: [[1,2,3]                
        [4,5,6]
        [7,8,9]]                   

Output: [[7,4,1]
        [8,5,2]
        [9,6,3]]
Explanation: Rotate the matrix simply by 90 degree clockwise and return the matrix.
'''

# Brute Force 
def rotateMatrix(matrix):
    '''
    n = len(matrix)
    second = [[0 for _ in range (n)] for _ in range(n)]
    
    for i in range (n):
        for j in range (n):
            second[j][n-i-1] = matrix[i][j] 
    return second
    '''
    n = len(matrix)
    m = len(matrix)
    rotated = [[0 for _ in range (m)] for _ in range (n)]

    for i in range (n):
        for j in range (m):
            rotated[j][n-i-1] = matrix[i][j]
    return rotated

# Test Run 
# print(rotateMatrix([[1,2,3],[4,5,6],[7,8,9]]))


# Optimal Approach
def rotateBy(matrix):
    # we first transpose the matrix when rotating a matrix 
    n = len(matrix)
    for i in range (n):
        for j in range (i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Step 2 : we reverse the array 
    for i in range (n):
        matrix[i].reverse()
    return matrix


# Test Run 
print(rotateBy([[1,2,3],[4,5,6],[7,8,9]]))

            
    
  
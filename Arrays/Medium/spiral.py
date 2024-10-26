'''
Coding Ninja : > https://www.codingninjas.com/studio/problems/spiral-matrix_6922069?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode : > https://leetcode.com/problems/spiral-matrix/description/
Problem Statement : Given a Matrix, print the given matrix in spiral order 
Input: Matrix[][] = { { 1, 2, 3, 4 },
		      { 5, 6, 7, 8 },
		      { 9, 10, 11, 12 },
	              { 13, 14, 15, 16 } }

Outhput: 1, 2, 3, 4,-> 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10.
Explanation: The output of matrix in spiral form.
'''

def spiral(matrix):
    n = len(matrix) 
    m = len(matrix[0])
    ans = []
    
    # Intial pointers for traversing 
    top = 0 
    left = 0 
    
    bottom = n-1 
    right = m-1 
     
    while (top<= bottom and left <= right):
        # For Moving from  left to right 
        for i in range (left,right+1):
            ans.append(matrix[top][i])
        top += 1
        
        # For moving top to bottom 
        for i in range (top,bottom+1):
            ans.append(matrix[i][right])                            #🥸🥸🥸🥸🥸🥸🥸🥸🥸🥸🥸💀💀💀💀💀💀💀
        right -= 1

        # For moving right to left
        if (top <= bottom):
            for i in range (right, left-1,-1):
                ans.append(matrix[bottom][i])
            bottom -= 1 
            
            
        # For moving top to bottom 
        if (left <= right):
            for i in range (bottom,top-1,-1):
                ans.append(matrix[i][left])
                
            left += 1
        
    return ans


# Test Run 
print(spiral( [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    
    
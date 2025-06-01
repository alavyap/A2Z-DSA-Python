'''
Link :> https://leetcode.com/problems/minimum-falling-path-sum/description/

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.
A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

Example 2:
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.
 

Constraints:
n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
'''
import sys

# Memoization
def minFalling(matrix): 
    
    m = len(matrix)
    n = len(matrix[0])
    dp = [[-1 for _ in range (n)] for _ in range (m)]
    mini = sys.maxsize  #NOTE - For finding Maximum it will be -sys.maxsize
    
    for j in range (m): 
        ans = helper(m-1,j,n,matrix,dp)
        mini = min(mini,ans)  #NOTE - For finding Maximun it will be Max(mini,ans)
    return mini 


def helper(i,j,n,matrix,dp): 
    
    if j < 0 or j >= n : 
        return int(1e9) #NOTE -  For finding Maximun it will be -int(1e9)
    if i == 0 : 
        return matrix[0][j]
    if dp[i][j] != -1 : 
        return dp[i][j] 
    
    up = matrix[i][j] + helper(i-1,j,n,matrix,dp)
    leftD = matrix[i][j] + helper(i-1,j-1,n,matrix,dp)
    rightD = matrix[i][j] + helper(i-1,j+1,n,matrix,dp)
    
    dp[i][j] = min(up,min(leftD,rightD))   #NOTE -  For finding Maximun it will be max(up, max(leftD, rightD))
    return dp[i][j]


# Tabulation

def minFall(matrix): 
    
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for _ in range (n)] for _ in range (m)]
    
    
    for j in range (n): 
        dp[0][j] = matrix[0][j] 
        
    for i in range (1,m): 
        for j in range (n):
            
            up = matrix[i][j] + dp[i-1][j] 
            
            leftD = matrix[i][j] 
            if j -1 >= 0 :
                leftD += dp[i-1][j-1]
            else: 
                leftD += int(1e9) #NOTE -  For Maximum it will be -int(1e9)
                
                    
            rightD = matrix[i][j] 
            if j+1 < n : 
                rightD += dp[i-1][j+1]
            else : 
                rightD += int(1e9) #NOTE -  For Maximum it will be -int(1e9)
            dp[i][j] = min(up,leftD,rightD) #NOTE -  For Maximum it will be max(up,leftD,rightD)
    mini = sys.maxsize #NOTE - For Maximum it will be -sys.maxsize
    for j in range (n): 
        mini = min(mini,dp[m-1][j])  #NOTE - For Maximum it will be min(mini,dp[m-1][j])
        
    return mini


# Space Optimizatino 

def fallingMin(matrix):
    
    m = len(matrix)
    n = len(matrix[0]) 
    
    prev = [0] * n 
    curr = [0] * m 
    
    for j  in range (n):
        prev[j] = matrix[0][j]
        
    for i in range (1,m):
        for j in range (n): 
            up = matrix[i][j] + prev[j] 
            
            leftD = matrix[i][j] 
            if j- 1 >= 0 : 
                leftD += prev[j-1]
            else: 
                leftD += int(1e9)
            rightD = matrix[i][j]
            
            if j +1 < m : 
                rightD += prev[j + 1]
            else: 
                rightD += int(1e9)
                
            curr[j] = min(up,leftD,rightD)
            
        prev = curr[:]
    mini = sys.maxsize
    for j in range (n): 
        mini = min(mini,prev[j])
    return mini
     
        
            
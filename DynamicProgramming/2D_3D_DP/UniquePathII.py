'''
Link :> https://leetcode.com/problems/unique-paths-ii/description/

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
 

Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
'''

# Memorization 

def uniquePaths(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[-1 for j in range (n)] for i in range (m)]
    return helper(m-1,n-1,obstacleGrid,dp)

def helper(i,j,obstacleGrid, dp):
        
    if i < 0 or j < 0 or obstacleGrid[i][j] == 1  : 
        return 0 
    if i == 0 and j == 0 : 
        return 1 
    if dp[i][j] != -1 : 
        return dp[i][j] 
    
    up = helper(i-1,j,obstacleGrid,dp)
    left = helper(i,j-1,obstacleGrid,dp)
    
    dp[i][j] = up + left 
    return dp[i][j] 


# Tabulation

def unique(obstacleGrid): 
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [[0] * n for _ in range (m)]
    
    if obstacleGrid[0][0] == 1 : 
        return 0 
    
    dp[0][0] = 1 
    
    for i in range (1,m): 
        if obstacleGrid[i][0] == 0 and dp[i-1][0] == 1 :
            dp[i][0] = 1
            
    for j in range (1,n): 
        if obstacleGrid[0][j] == 0 and dp[0][j-1] == 1 :
            dp[0][j] = 1 
            
    for i in range (1,m):
        for j in range (1,n): 
            if obstacleGrid[i][j] == 0 : 
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
    return dp[m-1][n-1]  


# Space Optimization 

def uniquesPace(obstacleGrid): 
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])  
    prev = [0] * n
    
    for i in range (m): 
        temp = [0] * n 
        
        for j in range (n): 
            if obstacleGrid[i][j] == 1 :
                temp[j] = 0
                continue
            
            if i == 0 and j == 0 : 
                temp[j] = 1 
                continue 
            up = 0 
            left = 0 
            
            if i > 0 :
                up = prev[j] 
            if j > 0 : 
                left = temp[j-1]
                
            temp[j] = up + left
        prev = temp 
    return prev[n-1]
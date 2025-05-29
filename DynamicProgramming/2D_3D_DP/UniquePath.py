'''
Link :> https://leetcode.com/problems/unique-paths/description/

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 

Example 1:
Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3 
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:

1 <= m, n <= 100
'''
def uniquePaths(m,n):
    dp = [[-1 for j in range (n)] for i in range (m)]
    return helper(m-1,n-1,dp)

def helper(i,j,dp):
    
    if i == 0 and j == 0 : 
        return 1 
    if i < 0 or j < 0 : 
        return 0 
    
    if dp[i][j] != -1 : 
        return dp[i][j] 
    
    up = helper(i-1,j,dp)
    left = helper(i,j-1,dp)
    
    dp[i][j] = up + left 
    return dp[i][j] 


# Tabulation 

def Paths(m,n):
    
    dp = [[-1 for j in range(n)] for i in range (m)]
    
    def helper(m,n,dp):
        for i in range (m):
            for j in range (n): 
                if i == 0 and j == 0 : 
                    dp[i][j] = 1 
                    continue     
                up =  0 
                left = 0 
                
                if i > 0 : 
                    up = dp[i-1][j] 
                    
                if j > 0 : 
                    left = dp[i][j-1]
                    
                dp[i][j] = up + left
        return dp[m-1][n-1]
    return helper(m,n,dp)       

# Space Optimization 
def unique(m,n): 
    prev = [0] * n
    for i in range (m):
        temp = [0] *n
        for j in range (n): 
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
'''
Link :> https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
'''
# Memoization 

def minPathSum(grid): 
    
    m = len(grid)
    n = len(grid[0])
    
    dp = [[-1 for j in range (n)] for _ in range (m)]
    return helper(m-1,n-1,grid,dp)


def helper(i,j,grid,dp): 
    
    if i == 0 and j == 0 : 
        return grid[0][0]
    
    if i < 0 or j < 0 : 
        return (float("inf"))
    
    if dp[i][j] != -1: 
        return dp[i][j] 
    
    up = grid[i][j] + helper(i-1,j,grid,dp)
    left = grid[i][j] + helper(i,j-1,grid,dp)
    
    dp[i][j] = min (up,left)
    return dp[i][j] 
    
    
# Tabulation 
def minSum(grid): 
    m = len(grid)
    n = len(grid[0])
    
    dp = [[0 for _ in range (n)] for _ in range (m)]
    
    for i in range (m):
        for j in range (n) : 
            
            if i == 0 and j == 0 : 
                dp[i][j] = grid[i][j] 
            else : 
                up = grid[i][j] 
                if i > 0 : 
                    up += dp[i-1][j] 
                    
                else: 
                    up += float("inf")
                
                left = grid[i][j] 
                if j > 0 : 
                    left += dp[i][j-1]
                else: 
                    left += float("inf")
                    
                dp[i][j] = min(up,left)
    return dp[m-1][n-1] 

# Space Optimization 
def sumMinPath(grid): 
    m = len(grid)
    n = len(grid[0]) 
    
    prev = [0] * n 
    for i in range (m): 
        temp = [0] * n
        
        for j in range (n): 
            if i == 0 and j == 0 : 
                temp[j] = grid[i][j] 
            else: 
                up = grid[i][j] 
                if i > 0 : 
                    up += prev[j] 
                else: 
                    up = float("inf")
                    
                left = grid[i][j]
                if j > 0 : 
                    left += temp[j-1]
                else: 
                    left = float("inf")
                temp[j] = min(up,left)
                
        prev = temp 
    return prev[n-1]
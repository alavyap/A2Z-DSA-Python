'''
Link :> https://leetcode.com/problems/triangle/


Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.
Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
 

Constraints:

1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-104 <= triangle[i][j] <= 104
 

Follow up: Could you do this using only O(n) extra space, where n is the total number of rows in the triangle?
'''

# Memoization
def minTotal(triangle):
   n = len(triangle)
   dp = [[-1 for _ in range (n)] for _ in range (n)]
   return helper(0,0,triangle,n,dp)

def helper(i,j,triangle,n,dp): 
   if dp[i][j] != -1: 
      return dp[i][j] 
   
   if i == n -1: 
      return triangle[i][j]
   
   down = triangle[i][j] + helper(i+1,j,triangle,n,dp)
   diagonal = triangle[i][j] + helper(i+1,j+1,triangle,n,dp)
   
   
   dp[i][j] = min(down,diagonal)
   return dp[i][j]



# Tabulation
def totalSum(triangle):
   n = len(triangle)
   dp = [[0 for _ in range (n)] for _ in range (n)]
   
   for j in range (n): 
      dp[n-1][j] = triangle[n-1][j] 
      
   for i in range (n-2,-1,-1): 
      for j in range (i,-1,-1): 
         
         down = triangle[i][j] + dp[i+1][j] 
         diagonal = triangle[i][j] + dp[i+1][j+1]     
         dp[i][j] = min(down,diagonal)
         
   return dp[0][0]


# Space Otimization
def minPath(triangle): 
   n = len(triangle)
   front = [0] * n 
   
   for j in range (n): 
      front[j] = triangle[n-1][j] 

   for i in range (n-2,-1,-1):
      cur = [0] * n 
      for j in range (i,-1,-1): 
         down = triangle[i][j] + front[j] 
         diagonal = triangle[i][j] + front[j+1]
         
         cur[j] = min(down,diagonal)
      front = cur 
      
   return front[0]
   
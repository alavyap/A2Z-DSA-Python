'''
Link :> https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''

def squares(matrix): 
    n = len(matrix)
    m = len(matrix[0])
    
    dp = [[0] * m for _ in range (n)]
    
    for j in range (m):
        dp[0][j] = matrix[0][j]
    for i in range (n):
        dp[i][0] = matrix[i][0]
        
    for i in range (1,n):
        for j in range (1,m): 
            if matrix[i][j] == 0: 
                dp[i][j] = 0 
            else: 
                dp[i][j] = 1 + min(dp[i-1][j],
                                   dp[i-1][j-1],
                                   dp[i][j-1])
                
    total = 0 
    for i in range (n):
        for j in range (m):
            total += dp[i][j] 
    return total
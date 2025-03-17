'''
Link :> https://leetcode.com/problems/surrounded-regions/description/

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.


Example 2:
Input: board = [["X"]]
Output: [["X"]]

 
Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''

def surroundedRegion(board):
    
    if not board or not board[0]:
        return 
    
    m = len(board)
    n = len(board[0])
    
    
    def dfs(i,j):
        if i <0 or i >= m or j < 0 or j >= n or board[i][j] != "O" :
            return 
        
        board[i][j]  = "T"
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)
         
    for i in range (m):
        dfs(i,0)
        dfs(i,n-1)
        
    for j in range (n):
        dfs(0,j)
        dfs(m-1,j)
        
    for i in range (m):
        for j in range (n):
            if board[i][j] == "O":
                board[i][j] = "X"
    
    for i in range (m):
        for j in range (n):
            if board[i][j] == "T" :
                board[i][j] = "O"
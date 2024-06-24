'''
LeetCode :> https://leetcode.com/problems/n-queens/description/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
 

Constraints:
1 <= n <= 9


'''

# Better Approach 
def main (n):
    
    ans = [] 
    board = ["." *n for _ in range (n)] 
    
    solve(0,board,ans,n)
    return ans 

def solve(self,col,board,ans,n):
    
    # Base Case 
    if col == n :
        ans.append(list(board))
        return 
    
    for row in range (n):
        if self.isSafe(row,col,board,n):
            board[row] = board[row][:col] + "Q" + board[row][col+1:]
            self.solve(col+1,board,ans,n)
            board[row] = board[row][:col] + "." + board[row][col+1:]
            
            
def isSafe(self,row,col,board,n):
    
    #check upper element
    duprow = row
    dupcol = col 
    
    # This will check every row if the that position has a Queen or not 
    while row >= 0 and col >= 0 :
        if board[row][col] == "Q":
            return False 
        row -= 1
        col -= 1
        
    # Now checking in every column if the queen is present or not 
    col = dupcol
    row = duprow
    while col >= 0 :
        if board[row][col] == "Q":
            return False 
        col -= 1 
        
        
    # Now cheking for every diagonal if the queen is present or not 
    row = duprow 
    col = dupcol 
    
    while row <  n and col >= 0 :
        if board[row][col] == "Q":
            return False
        row += 1 
        col -= 1
        
    return True
         
    
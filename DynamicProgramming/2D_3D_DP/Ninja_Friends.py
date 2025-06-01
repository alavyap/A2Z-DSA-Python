'''

Link :> https://www.naukri.com/code360/problems/ninja-and-his-friends_3125885?source=youtube&campaign=striver_dp_videos&leftPanelTab=0


Problem statement
Ninja has a 'GRID' of size 'R' X 'C'. Each cell of the grid contains some chocolates. Ninja has two friends Alice and Bob, and he wants to collect as many chocolates as possible with the help of his friends.

Initially, Alice is in the top-left position i.e. (0, 0), and Bob is in the top-right place i.e. (0, ‘C’ - 1) in the grid. Each of them can move from their current cell to the cells just below them. When anyone passes from any cell, he will pick all chocolates in it, and then the number of chocolates in that cell will become zero. If both stay in the same cell, only one of them will pick the chocolates in it.

If Alice or Bob is at (i, j) then they can move to (i + 1, j), (i + 1, j - 1) or (i + 1, j + 1). They will always stay inside the ‘GRID’.

Your task is to find the maximum number of chocolates Ninja can collect with the help of his friends by following the above rules.

Example:
Input: ‘R’ = 3, ‘C’ = 4
       ‘GRID’ = [[2, 3, 1, 2], [3, 4, 2, 2], [5, 6, 3, 5]]
Output: 21

Initially Alice is at the position (0,0) he can follow the path (0,0) -> (1,1) -> (2,1) and will collect 2 + 4 + 6 = 12 chocolates.

Initially Bob is at the position (0, 3) and he can follow the path (0, 3) -> (1,3) -> (2, 3) and will colllect 2 + 2 + 5 = 9 chocolates.

Hence the total number of chocolates collected will be 12 + 9 = 21. there is no other possible way to collect a greater number of chocolates than 21.
Detailed explanation ( Input/output format, Notes, Images )
Constraints :
1 <= ‘T’ <= 10
2 <= 'R', 'C' <= 50
0 <= 'GRID[i][j]'<= 10^2
Time Limit: 1sec
Sample Input 1 :
2
3 4
2 3 1 2
3 4 2 2
5 6 3 5
2 2
1 1
1 2
Sample Output 1 :
21
5
Explanation Of Sample Input 1 :
For the first test case, Initially Alice is at the position (0, 0) he can follow the path (0, 0) -> (1, 1) -> (2, 1) and will collect 2 + 4 + 6 = 12 chocolates.

Initially Bob is at the position (0, 3) and he can follow the path (0, 3) -> (1, 3) -> (2, 3) and will collect 2 + 2 + 5 = 9 chocolates.

Hence the total number of chocolates collected will be 12 + 9 = 21.

For the second test case, Alice will follow the path (0, 0) -> (1, 0) and Bob will follow the path (0, 1) -> (1, 1). total number of chocolates collected will be 1 + 1 + 1 + 2 = 5
Sample Input 2 :
2
2 2
3 7
7 6
3 2
4 5
3 7
4 2
Sample Output 2 :
23
25

'''

# Memoization
import sys


def maximun(r,c,grid): 
    
    dp = [[[-1 for _ in range(c)] for _ in range(c)] for _ in range(r)]
    return helper(0, 0, c - 1, r, c, grid, dp)

def helper(i, j1, j2, n, m, grid, dp):
    if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
        return -int(1e9)
    if i == n - 1:
        if j1 == j2:
            return grid[i][j1]
        else:
            return grid[i][j1] + grid[i][j2]
    
    if dp[i][j1][j2] != -1:
        return dp[i][j1][j2]

    maxi = -sys.maxsize
    for dj1 in range(-1, 2):
        for dj2 in range(-1, 2):
            new_j1 = j1 + dj1
            new_j2 = j2 + dj2
            value = 0
            if j1 == j2:
                value = grid[i][j1]
            else:
                value = grid[i][j1] + grid[i][j2]
            value += helper(i + 1, new_j1, new_j2, n, m, grid, dp)
            maxi = max(maxi, value)

    dp[i][j1][j2] = maxi
    return maxi

# Tabulation
def maxChoc(r,c,grid): 
    dp = [[[0 for _ in range(c)] for _ in range(c)] for _ in range(r)]

    # Base case: fill the last row
    for j1 in range(c):
        for j2 in range(c):
            if j1 == j2:
                dp[r - 1][j1][j2] = grid[r - 1][j1]
            else:
                dp[r - 1][j1][j2] = grid[r - 1][j1] + grid[r - 1][j2]

    # Fill the table from bottom to top
    for i in range(r - 2, -1, -1):
        for j1 in range(c):
            for j2 in range(c):
                maxi = -sys.maxsize
                for dj1 in range(-1, 2):
                    for dj2 in range(-1, 2):
                        nj1 = j1 + dj1
                        nj2 = j2 + dj2
                        if 0 <= nj1 < c and 0 <= nj2 < c:
                            if j1 == j2:
                                value = grid[i][j1]
                            else:
                                value = grid[i][j1] + grid[i][j2]
                            value += dp[i + 1][nj1][nj2]
                            maxi = max(maxi, value)
                dp[i][j1][j2] = maxi

    # Return result from the top-left and top-right starting positions
    return dp[0][0][c - 1]


# Space Optimization 
import sys

def maximumChocolates(r, c, grid):
    # Initialize two matrices: front (for current row) and cur (for next row)
    front = [[0] * c for _ in range(c)]
    cur = [[0] * c for _ in range(c)]

    # Base case: fill the last row
    for j1 in range(c):
        for j2 in range(c):
            if j1 == j2:
                front[j1][j2] = grid[r - 1][j1]
            else:
                front[j1][j2] = grid[r - 1][j1] + grid[r - 1][j2]

    # Fill from bottom row to top
    for i in range(r - 2, -1, -1):
        for j1 in range(c):
            for j2 in range(c):
                maxi = -sys.maxsize

                for dj1 in range(-1, 2):
                    for dj2 in range(-1, 2):
                        nj1 = j1 + dj1
                        nj2 = j2 + dj2

                        if 0 <= nj1 < c and 0 <= nj2 < c:
                            if j1 == j2:
                                value = grid[i][j1]
                            else:
                                value = grid[i][j1] + grid[i][j2]
                            value += front[nj1][nj2]
                            maxi = max(maxi, value)
                cur[j1][j2] = maxi

        # Move to next row
        front = [row[:] for row in cur]

    return front[0][c - 1]

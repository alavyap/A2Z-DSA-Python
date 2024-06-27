'''
GFG :> https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

Problem :> Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:
Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.
Example 2:
Input:
N = 2
m[][] = {{1, 0},
         {1, 0}}
Output:
-1
Explanation:
No path exists and destination cell is 
blocked.
Your Task:  
You don't need to read input or print anything. Complete the function printPath() which takes N and 2D array m[ ][ ] as input parameters and returns the list of paths in lexicographically increasing order. 
Note: In case of no path, return an empty list. The driver will output "-1" automatically.

Expected Time Complexity: O((3N^2)).
Expected Auxiliary Space: O(L * X), L = length of the path, X = number of paths.

Constraints:
2 ≤ N ≤ 5
0 ≤ m[i][j] ≤ 1

'''
# Recursion , Backtracking  
# Time :. O(4 ^(N*M)) ;; Space :. O(N*M)
def path_find(m,n):
    ans = []
    board = [[0 for _ in range(n)] for _ in range (n)]
    
    if m[0][0] == 1 :
        backtrack(0, 0, m, n, ans, "", board)
        
    return ans 

def backtrack(self,i,j,a,n,ans,move,vis):
    if i == n-1 and j == n-1 : 
        ans.append(move)
        return 
    
    
    # Downward 
    if i+1 < n and not vis[i+1][j] and a[i+1][j] == 1 :
        vis[i][j] = 1 
        self.backtrack(i+1,j,a,n,ans,move + "D",vis)
        vis[i][j] = 0 
        
    # Left 
    if j - 1 >= 0 and not vis[i][j-1] and a[i][j-1] == 1 :
        vis[i][j] = 1
        self.backtrack(i,j-1,a,n,ans,move + "L",vis)
        vis[i][j] = 0
        
    # Right
    if j + 1 < n and not vis[i][j+1] and a[i][j+1] == 1 :
        vis[i][j] = 1
        self.backtrack(i,j+1,a,n,ans,move + "R", vis)
        vis[i][j] = 0 
        
    # Upward 
    if i - 1 >= 0 and not vis[i-1][j] and a[i-1][j] == 1 :
        vis[i][j] = 1
        self.backtrack(i-1,j,a,n, ans, move + "U", vis )
        vis[i][j] = 0


# Optimal Approach

def find_path(self,m,n):
    ans = [] 
    board = [[0 for _ in range (n)] for _ in range(n)]
    
    di = [+1,0,0,-1]
    dj = [0,-1,1,0]
    
    if m[0][0] == 1 :
        self.helper(0,0,m,n,ans,"",board,di,dj)
    return ans 

def helper(self,i,j,a,n,ans,move,vis,di,dj):
    if i == n-1 and j == n-1 :
        ans.append(move)
        return 
    
    dire = "DLRU"
    
    for indx in range (4):
        nexti = i +di[indx]
        nextj = j + dj[indx]
        
        if nexti >= 0 and nextj >= 0 and nexti < n and nextj < n and not vis[nexti][nextj] and a[nexti][nextj] == 1 :
            vis[i][j] = 1 
            self.helper(nexti,nextj,a,n,ans,move+ dire[indx],vis,di,dj)
            vis[i][j] = 0


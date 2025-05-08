'''
Link :> https://leetcode.com/problems/making-a-large-island/description/

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:
Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:
Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.



'''
class DSU: 
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1] *n 
        
    def find (self,x):
        if self.parent[x] != x: 
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x] 
    
    
    def union(self,x,y):
        xr,yr = self.find(x),self.find(y)
        if xr == yr :
            return 
        if self.size[xr] < self.size[yr]:
            xr,yr = yr,xr 
        self.parent[yr] = xr 
        self.size[xr] += self.size[yr]
        
        
def mainFunction(grid): 
    n = len(grid)
    dsu = DSU(n*n)
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    
    # Step 1 : Union of all 1s 
    for r in range (n): 
        for c in range (n):
            if grid[r][c] == 1 : 
                for dr,dc in directions: 
                    nr,nc = r + dr,  c + dc
                    if 0 <= nr < n  and 0 <= nc < n and grid[nr][nc] == 1 : 
                        dsu.union(r * n + c, nr * n +nc)
                        
    #  Step 2 : Count the size of each island 
    island_size = {} 
    for r in range (n): 
        for c in range (n): 
            if grid[r][c] == 1 :
                root = dsu.find(r * n +c)
                island_size[root] = dsu.size[root]
                
    maxArea = max(island_size.values(), default= 0 )
    
    
    # Step 3 : Try flipping each 0 to 1 
    for r in range (n):
        for c in range (n): 
            if grid[r][c] == 0 : 
                seen = set() 
                area = 1 #flipping this 0 
                
                for dr,dc in directions: 
                    nr,nc = r + dr,c +dc 
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1 :
                        root = dsu.find(nr * n + nc )
                        if root not in seen :
                            seen.add(root)
                            area += dsu.size[root]
                            
                maxArea = max(maxArea,area)
                
                
    return maxArea
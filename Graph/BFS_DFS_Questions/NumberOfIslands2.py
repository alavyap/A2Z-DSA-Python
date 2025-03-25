'''
Link :> https://leetcode.com/problems/number-of-distinct-islands-ii/description/  ||        https://www.lintcode.com/problem/804/

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if they have the same shape, or have the same shape after rotation (90, 180, or 270 degrees only) or reflection (left/right direction or up/down direction).

The length of each dimension in the given grid does not exceed 50.

Example
Example 1:

Input: [[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]
Output: 1
Explanation:
The island is look like this:
11000
10000
00001
00011

Notice that:
11
1
and
 1
11
are considered same island shapes. Because if we make a 180 degrees clockwise rotation on the first island, then two islands will have the same shapes.
Example 2:

Input: [[1,1,1,0,0],[1,0,0,0,1],[0,1,0,0,1],[0,1,1,1,0]]
Output: 2
Explanation:
The island is look like this:
11100
10001
01001
01110

Here are the two distinct islands:
111
1
and
1
1

Notice that:
111
1
and
1
111
are considered same island shapes. Because if we flip the first array in the up/down direction, then they have the same shapes.

'''

# Brute Force 

import queue


class BruteForce :
    
    def numDistinctIsland(grid):
        
        if not grid or not grid[0] :
            return 0 
        rows,cols = len(grid),len(grid[0])
        
        visited = set() 
        
        unique_islands = set() 
        
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        
        def find_island(r,c):
            
            island = [] 
            queue = [(r,c)]
            visited.add((r,c))
            
            while queue:
                curr_r,curr_c = queue.pop(0)
                
                island.append((curr_r-r, curr_c-c))
                
                for dr,dc in directions:
                    nr,nc = curr_r + dr, curr_c + dc
                    if(0 <= nr <rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr,nc) not in visited):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            return island  
        
        
        
        def generate_transformation(island):
            
            transformations = [] 
            
            for reflect_x in [1,-1]:
                for reflect_y in [1,-1]:
                    
                    for rotation in range(4):
                        transformed =[] 
                        
                        for x,y in island :
                            nx = reflect_x * x 
                            ny = reflect_y * y 
                            
                            for _ in range (rotation):
                                nx,ny = ny,-nx
                                
                                transformed.append((nx,ny))
                                
                        min_x = min(x for x, _ in transformed)
                        min_y = min(y for _, y in transformed)
                        normalized = tuple(sorted((x - min_x, y - min_y) for x,y in transformed))
                        
                        transformations.append(normalized)
                        
            return min(transformations)
        
        
        for r in range (rows):
            for c in range (cols):
                if grid[r][c] == 1 and (r,c) not in visited :
                    
                    island = find_island(r,c)
                    
                    canonical_form = generate_transformation(island)
                    unique_islands.add(canonical_form)
                    
        return len(unique_islands)
    

# Optimal Approach 

class Solution: 
    
    def numDistinctIslands(grid):
        
        if not grid or not grid[0]:
            return 0 
        
        rows,cols = len(grid),len(grid[0])
        visited = [[False] * cols for _ in range (rows)]
        unique_islands = set() 
        
        
        def dfs(r,c):
            
            if(r< 0 or r >= rows or c < 0 or c>= cols or grid[r][c] == 0 or visited[r][c]):
                return [] 

            visited[r][c] = True 
            
            island = [(0,0)]
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            
            for dr,dc in directions: 
                nr,nc = r + dr, c+ dc
                sub_island = dfs(nr,nc)
                
                island.extend([(x+dr, y+dc) for x,y in sub_island])
            return island 
        
        
        def normalize(island):
            
            shapes = [] 
            
            for i in range(8):
                transformed = [] 
                for x,y in island: 
                    
                    if i == 0 : transformed.appen((x,y))
                    elif i == 1 : transformed.append((x,-y))
                    elif i == 2 : transformed.append((-x,y))
                    elif i == 3: transformed.append((-x,-y))
                    elif i == 4: transformed.append((y,x))
                    elif i == 5 : transformed.append(y,-x)
                    elif i == 6 : transformed.append((-y,x))
                    elif i == 7 : transformed.append((-y,-x))
                    
                    
                min_x = min(x for x, _ in transformed)
                min_y = min(y for _ , y in transformed)
                normalized = [(x - min_x, y - min_y) for x,y in transformed]
                
                normalized.sort() 
                shapes.append(tuple(normalized))
                
            return min(shapes) 
        
        for r in range(rows):
            for c in range (cols):
                if grid[r][c] == 1 and not visited[r][c] :
                    island = dfs(r,c)
                    
                    
                    if island: 
                        canonical_form = normalize(island)
                        unique_islands.add(canonical_form)
        return len(unique_islands)   

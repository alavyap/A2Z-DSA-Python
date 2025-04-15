'''
Link :> https://leetcode.com/problems/path-with-minimum-effort/description/

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Example 2:
Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].

Example 3:
Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.
 

Constraints:
rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106

'''

# Brute Force 
from collections import deque
import heapq
from multiprocessing import heap


def bruteMin(heights):
    rows,cols = len(heights),len(heights[0])
    
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    
    def canReach(maxEffort):
        visited = [[False] * cols for _ in range (rows)]
        queue = deque() 
        queue.append((0,0))
        visited[0][0] = True 
        
        while queue : 
            x,y = queue.popleft() 
            if x == rows -1 and y == cols -1 : 
                return True
            for dx,dy in directions : 
                nx,ny = x+dx, y+dy 
                if (0 <=nx <rows) and (0 <= ny < cols) and not visited[nx][ny]: 
                    if abs(heights[nx][ny] - heights[x][y]) <= maxEffort : 
                        visited[nx][ny] = True 
                        queue.append((nx,ny))
        return False 
    
    
    left, right = 0 , 10** 6 
    result = right 
    
    while left <= right : 
        mid = (left+right) // 2 
        if canReach(mid):
            result = mid 
            right = mid -1 
        else :
            left = mid +1 
    return result 


# Optimal Code 

def optimalMin(heights): 
    rows,cols = len(heights), len(heights[0]) 
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    
    effort = [[float("inf")] * cols for _ in range (rows)]
    effort[0][0] = 0 
    
    minHeap = [(0,0,0)]
    
    while minHeap :
        currEffort,x,y = heapq.heappop(minHeap)
        
        if x == rows -1 and y == cols -1 : 
            return currEffort
        
        for dx,dy in directions :
            nx,ny = x + dx ,y + dy 
            
            if 0 <= nx < rows and 0 <= ny < cols : 
                nextEffort = max(currEffort,abs(heights[nx][ny] - heights[x][y]))
                
                if nextEffort < effort[nx][ny] :
                    effort[nx][ny] = nextEffort 
                    heapq.heappush(minHeap,(nextEffort,nx,ny))
                    
    return 0 
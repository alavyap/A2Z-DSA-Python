'''

Link :> https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.
 

Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 104
No two stones are at the same coordinate point.
'''

class DisjointSet:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n 
        self.count = n 
    
    def find(self,i):
        if self.parent[i] != i :
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i] 
    
    def union(self,i,j):
        rootI = self.find(i)
        rootJ = self.find(j)
        if rootI != rootJ : 
            if self.rank[rootI] < self.rank[rootJ]:
                self.parent[rootI] = rootJ 
            elif self.rank[rootI] > self.rank[rootJ]:
                self.parent[rootJ] = rootI 
            else : 
                self.parent[rootJ] = rootI 
                self.rank[rootI] += 1 
            self.count -= 1 
            return True 
        return False 
        
def removeStones(stones):     
     
    n = len(stones)
    ds = DisjointSet(n)
    rowMap = {} 
    colMap = {} 
    
    for i in range(n): 
        x,y = stones[i]
        if x in rowMap:
            ds.union(i,rowMap[x])
        else: 
            rowMap[x] = i 
        if y in colMap: 
            ds.union(i,colMap[y])
        else: 
            colMap[y] = i 
            
    return n - ds.count
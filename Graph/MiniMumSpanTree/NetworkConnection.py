'''
Link :> https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

 
Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
 

Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.
'''

# DisJoint Set 
class DSU: 
    
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] * n 
    
    def find(self,x):
        if self.parent[x] != x :
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x] 
    
    def union (self,x,y):
        xr,yr = self.find(x),self.find(y)
        if xr == yr : 
            return False 
        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr 
        elif self.rank[xr] > self.rank[yr]: 
            self.parent[yr] = xr 
        else: 
            self.parent[yr] = xr 
            self.rank[xr] += 1 
        return True 
    
    
def mainFunction(n,connections):
    if len(connections) < n -1 : 
        return -1 
    dsu = DSU(n)
    components = n 
    
    for a,b in connections: 
        if dsu.union(a,b): 
            components -= 1 
    return components -1 
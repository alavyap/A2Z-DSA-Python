'''

Link :> https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

Given an undirected graph with V vertices labelled from 0 to V-1 and E edges, check whether the graph contains any cycle or not. The Graph is represented as an adjacency list, where adj[i] contains all the vertices that are directly connected to vertex i.

NOTE: The adjacency list represents undirected edges, meaning that if there is an edge between vertex i and vertex j, both j will be adj[i] and i will be in adj[j].

Examples:

Input: adj = [[1], [0,2,4], [1,3], [2,4], [1,3]] 
Output: 1
Explanation: 

1->2->3->4->1 is a cycle.
Input: adj = [[], [2], [1,3], [2]]
Output: 0
Explanation: 

No cycle in the graph.
Constraints:
1 ≤ adj.size() ≤ 105
''' 

# BFS Approach
from collections import deque


def bfsCycle(V,adj):
    
    visited = [False] * V
    def bfs(start):
        queue = deque()
        queue.append((start,-1))
        visited[start] = True
        
        while queue: 
            node,parent = queue.popleft()
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor,node))
                elif neighbor != parent :
                    return True
        return False
    
    for i in range (V):
        if not visited[i] :
            if bfs(i):
                return 1
    return 0 
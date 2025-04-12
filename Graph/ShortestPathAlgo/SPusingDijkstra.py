'''
Link :> https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1

You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges along with their weights. Find the shortest weight path between the vertex 1 and the vertex n,  if there exists a path, and return a list of integers whose first element is the weight of the path, and the rest consist of the nodes on that path. If no path exists, then return a list containing a single element -1.

The input list of edges is as follows - {a, b, w}, denoting there is an edge between a and b, and w is the weight of that edge.

Note: The driver code here will first check if the weight of the path returned is equal to the sum of the weights along the nodes on that path, if equal it will output the weight of the path, else -2. In case the list contains only a single element (-1) it will simply output -1. 

Examples :

Input: n = 5, m= 6, edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
Output: 5
Explanation: Shortest path from 1 to n is by the path 1 4 3 5 whose weight is 5. 
Input: n = 2, m= 1, edges = [[1, 2, 2]]
Output: 2
Explanation: Shortest path from 1 to 2 is by the path 1 2 whose weight is 2. 
Input: n = 2, m= 0, edges = [ ]
Output: -1
Explanation: Since there are no edges, so no answer is possible.
Expected Time Complexity: O(m* log(n))
Expected Space Complexity: O(n+m)

Constraint:
2 <= n <= 106
0 <= m <= 106
1 <= a, b <= n
1 <= w <= 105
'''

import heapq
import sys


def spDijkstra(n,m,edges):
    
    graph = {i : [] for i in range (1,n +1)}

    for a,b,w in edges:
        graph[a].append((b,w))
        graph[b].append((a,w))
            
    dist = {i : sys.maxsize for i in range(1,n+1)}  
    dist[1] = 0 
    parent = {i : None for i in range(1,n +1)}
    pq = [(0,1)]
    
    while pq : 
        currentDist,u = heapq.heappop(pq)
        
        if u == n :
            break 
        
        if currentDist > dist[u] : 
            continue       
        
        for v,weight in graph[u] : 
            newDist = currentDist + weight
            if newDist < dist[v]:
                dist[v] = newDist
                parent[v] = u 
                heapq.heappush(pq,(newDist,v))
                
    if dist[n] == sys.maxsize :
        return[-1]
        
    path=[]
    node = n 
    while node is not None :
        path.append(node)
        node = parent[node]
            
    path.reverse()           
    return [dist[n]] + path
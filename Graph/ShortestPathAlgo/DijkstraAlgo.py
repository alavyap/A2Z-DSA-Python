'''
Link :> https://www.geeksforgeeks.org/problems/implementing-dijkstra-set-1-adjacency-matrix/1


Given an undirected, weighted graph with V vertices numbered from 0 to V-1 and E edges, represented by 2d array edges[][], where edges[i]=[u, v, w] represents the edge between the nodes u and v having w edge weight.
You have to find the shortest distance of all the vertices from the source vertex src, and return an array of integers where the ith element denotes the shortest distance between ith node and source vertex src.

Note: The Graph is connected and doesn't contain any negative weight edge.

Examples:

Input: V = 3, edges[][] = [[0, 1, 1], [1, 2, 3], [0, 2, 6]], src = 2
Output: [4, 3, 0]
Explanation:

Shortest Paths:
For 2 to 0 minimum distance will be 4. By following path 2 -> 1 -> 0
For 2 to 1 minimum distance will be 3. By following path 2 -> 1
For 2 to 2 minimum distance will be 0. By following path 2 -> 2
Input: V = 5, edges[][] = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]], src = 0
Output: [0, 4, 8, 10, 10]
Explanation: 

Shortest Paths: 
For 0 to 1 minimum distance will be 4. By following path 0 -> 1
For 0 to 2 minimum distance will be 8. By following path 0 -> 2
For 0 to 3 minimum distance will be 10. By following path 0 -> 2 -> 3 
For 0 to 4 minimum distance will be 10. By following path 0 -> 1 -> 4
Constraints:
1 ≤ V ≤ 105
1 ≤ E = edges.size() ≤ 105
0 ≤ edges[i][j] ≤ 104
0 ≤ src < V
'''

from collections import defaultdict
import heapq


def dijkstra(V,edges,src): 
    
    graph = defaultdict(list)
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w)) # Because the graph is undirected
        
    # Step 2 : Initialize distance array and priority queue 
    dist = [float("inf")] * V 
    dist[src] = 0 
    minHeap = [(0,src)] # (distance,node)
    
    
    while minHeap: 
        d,u = heapq.heappop(minHeap)
        
        if d > dist[u]: 
            continue  #Skip Outdated Entry
        
        for v,w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w 
                heapq.heappush(minHeap,(dist[v],v))
                
    return dist
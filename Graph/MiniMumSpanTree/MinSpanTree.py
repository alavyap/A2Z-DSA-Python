'''
Link :> https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

Given a weighted, undirected, and connected graph with V vertices and E edges, your task is to find the sum of the weights of the edges in the Minimum Spanning Tree (MST) of the graph. The graph is represented by an adjacency list, where each element adj[i] is a vector containing vector of integers. Each vector represents an edge, with the first integer denoting the endpoint of the edge and the second integer denoting the weight of the edge.

Input:
3 3
0 1 5
1 2 3
0 2 1
 
Output: 4
Explanation:
The Spanning Tree resulting in a weight
of 4 is shown above.

Input: 
2 1
0 1 5
Output: 5 

Explanation: Only one Spanning Tree is possible which has a weight of 5.
Constraints:
2 ≤ V ≤ 1000
V-1 ≤ E ≤ (V*(V-1))/2
1 ≤ w ≤ 1000
The graph is connected and doesn't contain self-loops & multiple edges.
'''

def mst(V,adj):
    edges = [[] for _ in range(V)]
    
    for u in range(V): 
        for vw in adj[u] :
            v,w = vw 
            edges[u].append((v,w))
        
    visited = [False] *V 
    visited[0] = True 
    mstWeight = 0 
    while sum(visited) < V :
        
        minW = float("inf")
        next = -1 
        
        for u in range(V):
            if visited[u]: 
                for v,w in edges[u]:
                    if not visited[v] and w < minW :
                        minW = w 
                        next = v 
                                              
        if next == -1 : 
            break 
        visited[next] = True 
        mstWeight += minW
    return mstWeight


# Upon Submitting  We get >>>
# Test Cases Passed: 
# 61 /71
# Time limit exceeded.

# Your program took more time than expected.Expected Time Limit : 1.72sec
# Hint : Please optimize your code and submit again.
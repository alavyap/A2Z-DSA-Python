'''
Link :> https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1

Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as an adjacency list, where adj[i] contains a list of vertices that are directly reachable from vertex i. Specifically, adj[i][j] represents an edge from vertex i to vertex j.

Example 1:

Input: 0 -> 1-> 2 -> 3 -> 3
Output: 1
Explanation: 3 -> 3 is a cycle


Example 2:
Input: 0 -> 1 -> 2 
Output: 0
Explanation: no cycle in the graph
Constraints:
1 ≤ V, E ≤ 105
'''

from collections import deque


def isCycle(adj):
    # Step 1: Compute inDegree of each node
    V = len(adj)
    inDegree = [0] * V 
    for u in range (V):
        for v in adj[u]:
            inDegree[v]  += 1 #Increment inDegree
            
    # Step 2 : Push nodes with inDegree 0 into queue
    queue = deque(i for i in range (V) if inDegree[i] == 0)
    count = 0  # To track number of nodes processed
    
    # Step 3 : Process the queue
    while queue: 
        node = queue.popleft() 
        count += 1 #Increment processed nodes count 
        
        for neighbor in adj[node]:
            inDegree[neighbor] -= 1  #Reduce inDegree
            if inDegree[neighbor] == 0 :
                queue.append(neighbor)
         
    # Step 4 : If all Nodes were processed, no cycle exists    
    return count != V  #If Count < V cycle Exists
                
            
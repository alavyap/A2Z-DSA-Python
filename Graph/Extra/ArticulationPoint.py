'''
Link :> https://www.geeksforgeeks.org/problems/articulation-point-1/1

Given an undirected connected graph with V vertices and adjacency list adj. You are required to find all the vertices removing which (and edges through it) disconnects the graph into 2 or more components and return it in sorted manner.
Note: Indexing is zero-based i.e nodes numbering from (0 to V-1). There might be loops present in the graph.

Example 1:

Input:

Output:{1,4}
Explanation: Removing the vertex 1 will
discconect the graph as-

Removing the vertex 4 will disconnect the
graph as-

 

Your Task:
You don't need to read or print anything. Your task is to complete the function articulationPoints() which takes V and adj as input parameters and returns a list containing all the vertices removing which turn the graph into two or more disconnected components in sorted order. If there are no such vertices then returns a list containing -1.
 

Expected Time Complexity: O(V + E)
Expected Auxiliary Space: O(V)
 

Constraints:
1 ≤ V ≤ 105
'''

def articulationPoints(V,adj):
    
    visited = [False] * V 
    disc = [float("inf")] * V 
    low =  [ float("inf")] * V 
    ap = [False] * V 
    time = 0 
    
    def dfs(node,parent): 
        nonlocal time 
        visited[node] = True 
        disc[node] = low [node] = time 
        time += 1 
        children = 0 
        
        for v in adj[node]: 
            if v == parent: 
                continue 
            if not visited[v] : 
                children += 1 
                dfs(v,node)
                low[node] = min(low[node],low[v])
                
                if parent != -1 and low[v] >= disc[node]:
                    ap[node]= True 
            else : 
                low[node] =min(low[node],disc[v])
                
                
        if parent == -1 and children > 1: 
            ap[node] = True 
            
    for i in range (V):
        if not visited[i] : 
            dfs(i,-1)
    result = [i for i, is_ap in enumerate(ap) if is_ap]
    return result if result else [-1]
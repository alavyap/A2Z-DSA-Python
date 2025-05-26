'''
Link :> https://www.geeksforgeeks.org/problems/strongly-connected-components-kosarajus-algo/1

Given an adjacency list, adj of Directed Graph, Find the number of strongly connected components in the graph.
 

Examples :

Input: adj[][] = [[2, 3], [0], [1], [4], []]

Output: 3
Explanation: We can clearly see that there are 3 Strongly Connected Components in the Graph.
 
Input: adj[][] = [[1], [2], [0]]

Output: 1
Explanation: All of the nodes are connected to each other. So, there's only one SCC.
Input: adj[][] = [[1], []]
Output: 2
Constraints:
2<=adj.size()<=106
0<=edges<=adj.size()-1

'''

def kosaraju(adj):
    
    def dfs(v,visited,stack):
        visited[v] = True 
        for u in adj[v]: 
            if not visited[u]: 
                dfs(u,visited,stack)
        stack.append(v)
        
    def reverse_graph(V,adj):
        rev = [[] for _ in range (V)]
        for v in range(V): 
            for u in adj[v]:
                rev[u].append(v)
        return rev
    
    
    def dfs_rev(v,visited,rev_adj):
        visited[v] = True 
        for u in rev_adj[v]: 
            if not visited[u]: 
                dfs_rev(u,visited,rev_adj)
    
    V = len(adj)
    visited = [False] * V 
    stack = [] 
    
    for i in range (V): 
        if not visited[i] :
            dfs(i,visited,stack)
            
    rev_adj = reverse_graph(V,adj)
    
    
    visited = [False] * V 
    scc_count = 0 
    while stack : 
        node = stack.pop() 
        if not visited[node]:
            dfs_rev(node,visited,rev_adj)
            scc_count += 1 
            
    return scc_count    
            
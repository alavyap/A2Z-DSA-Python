'''
Link :> https://www.lintcode.com/problem/3651/

Description
In this problem, there is an undirected graph with n nodes. There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.
You need to return the number of connected components in that graph.

Example
Example 1
Input:
3
[[0,1], [0,2]]
Output:
1

Example 2
Input:
6
[[0,1], [1,2], [2, 3], [4, 5]]
Output:2
'''

def counter(n,edges):
    
    from collections import defaultdict
    
    graph = defaultdict(list)
    for u,v in edges:
        graph[u].append(v) 
        graph[v].append(u) 
        
    
    visited = set()
    components = 0
    
    
    
    # DFS Function
    def dfs(node):
        stack = [node]
        
        while stack:
            current = stack.pop() 
            if current not in visited:
                visited.add(current)
                stack.extend(graph[current])
                
    # Count Connected components
    for i in range(n):
        if i not in visited:
            dfs(i)
            components += 1 
            
    return components
            
    
    



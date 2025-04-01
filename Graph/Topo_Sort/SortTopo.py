'''
Link :> https://www.geeksforgeeks.org/problems/topological-sort/1


Given an adjacency list for a Directed Acyclic Graph (DAG) where adj[u] contains a list of all vertices v such that there exists a directed edge u -> v. Return topological sort for the given graph.

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v, vertex u comes before v in the ordering.
Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be 1 else 0.

Examples:

Input: adj = [[], [0], [0], [0]] 

Output: 1
Explanation: The output 1 denotes that the order is valid. Few valid Topological orders for the given graph are:
[3, 2, 1, 0]
[1, 2, 3, 0]
[2, 3, 1, 0]
Input: adj = [[], [3], [3], [], [0,1], [0,2]]

Output: 1
Explanation: The output 1 denotes that the order is valid. Few valid Topological orders for the graph are:
[4, 5, 0, 1, 2, 3]
[5, 2, 4, 0, 1, 3]
Constraints:
2  ≤  V  ≤  103
1  ≤  E  ≤  (V * (V - 1)) / 2
'''

# Brute Force 

from itertools import permutations

def main_function(adj):
    vertices = list(range(len(adj)))
    
    for perm in permutations(vertices):
        if is_valid_topological_order(perm,adj):
            return list(perm)
    
    return None

def is_valid_topological_order(order,adj):
    position = {vertex: idx for idx,vertex in enumerate(order)}
    for u in range (len(adj)):
        for v in adj[u]:
            if position[u] > position[v] :
                return False 
            
    return True 


# Optimal Approach 
def topologicalSort(adj):
    
    v = len(adj) 
    visited = [False] * v 
    stack = [] 
    
    
    for ele in range (v): 
        if not visited[ele]: 
            dfs(ele,adj,visited,stack)
            
    return stack[::-1]


def dfs(vertex,adj,visited,stack):
    visited[vertex] = True 
    
    for neighbor in adj[vertex]:
        if not visited[neighbor]:
            dfs(neighbor,adj,visited,stack)
    stack.append(vertex)
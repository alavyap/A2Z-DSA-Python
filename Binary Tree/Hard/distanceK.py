'''

LeetCode :> https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
Output: [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
Example 2:

Input: root = [1], target = 1, k = 3
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 500].
0 <= Node.val <= 500
All the values Node.val are unique.
target is the value of one of the nodes in the tree.
0 <= k <= 1000

'''



def distance(root,target,k):
    
    parent_track = {} 
    
    def find_target_and_parent(node,parent=None):
        if not node :
            return None 
        
        parent_track[node] = parent
        
        
        if node.val == target.val :
            return node 
        
        left = find_target_and_parent(node.left,node)
        right = find_target_and_parent(node.right,node)
        
        return left if left else right
    
    def find_nodes_at_k_distance() :
        from collections import deque 
        queue = deque([(target_node,0)])
        
        visited = {target} 
        result = [] 
        
        while queue :
            node,dist = queue.popleft()
            
            if dist == k :
                result.append(node.val)
                continue 
            
            if node.left and node.left not in visited :
                visited.add(node.left)
                queue.append((node.left, dist +1))
            
            if node.right and node.right not in visited :
                visited.add(node.right)
                queue.append((node.right, dist +1 ))
                
            if node in parent_track and parent_track[node] and parent_track[node] not in visited:
                visited.add(parent_track[node])
                queue.append((parent_track[node], dist + 1))
        return result
                 
    
    
    
    target_node = find_target_and_parent(root)
    
    if not target_node : 
        return [] 
    return find_nodes_at_k_distance()
    
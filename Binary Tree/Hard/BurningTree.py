'''
GFG :> https://www.geeksforgeeks.org/problems/burning-tree/1

Given a binary tree and a node data called target. Find the minimum time required to burn the complete binary tree if the target is set on fire. It is known that in 1 second all nodes connected to a given node get burned. That is its left child, right child, and parent.
Note: The tree contains unique values.


Examples : 

Input:      
          1
        /   \
      2      3
    /  \      \
   4    5      6
       / \      \
      7   8      9
                   \
                   10
Target Node = 8
Output: 7
Explanation: If leaf with the value 8 is set on fire. 
After 1 sec: 5 is set on fire.
After 2 sec: 2, 7 are set to fire.
After 3 sec: 4, 1 are set to fire.
After 4 sec: 3 is set to fire.
After 5 sec: 6 is set to fire.
After 6 sec: 9 is set to fire.
After 7 sec: 10 is set to fire.
It takes 7s to burn the complete tree.
Input:      
          1
        /   \
      2      3
    /  \      \
   4    5      7
  /    / 
 8    10
Target Node = 10
Output: 5

Expected Time Complexity: O(number of nodes)
Expected Auxiliary Space: O(height of tree)


Constraints:
1 ≤ number of nodes ≤ 105

1 ≤ values of nodes ≤ 105


'''

from collections import deque


def treeBurn(root,target):
    
    parent_node = {}
    
    def find_parent(root):
       
        
        if not root :
            return None 
        
        queue = deque([(root)])
        target_node = None 
        
        while queue :
            node = queue.popleft()
            
            if node.val == target :
                target_node = node 
                
            if node.left :
                parent_node[node.left] = node 
                queue.append(node.left)
                
            if node.right :
                parent_node[node.right] = node 
                queue.append(node.right)
        
        return target_node
    
    def burned_time(target_node):
        timer = 0 
      
        visited = {target_node}
        queue = deque([target_node])
        
        while queue : 
            size = len(queue)
            burned_something = False 
            
            for _ in range (size) :
                node = queue.popleft() 
                
                if node in parent_node and parent_node[node] not in visited :
                    visited.add(parent_node[node])
                    queue.append(parent_node[node])
                    burned_something = True
                
                
                if node.left and node.left not in visited :
                    visited.add(node.left)
                    queue.append(node.left)
                    burned_something = True 
                    
                
                if node.right and node.right not in visited :
                    visited.add(node.right)
                    queue.append(node.right)
                    burned_something = True 
                    
                    
            if burned_something :
                timer += 1
        return timer
           

    
    if not root :
        return 0 
    
    burned_node = find_parent(root)
    
    return burned_time(burned_node)
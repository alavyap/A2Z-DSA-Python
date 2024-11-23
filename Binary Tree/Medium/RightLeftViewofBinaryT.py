'''
LeetCode :> https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

'''


def viewR(root):
    
    if not root :
        return [] 
    
    
    position = {} 
    
    queue = [(root,0)]
    max_level = 0
  
  
    
    while queue :
        
        node,level = queue.pop(0)
        position[level] = node.val 
        
        max_level = max(max_level,level)
        
        
        if node.left :
            queue.append((node.left, level +1))
            
        if node.right :
            queue.append((node.right,level+1))
            
            
    return [position[level] for level in range (max_level + 1)]



# Left Side 

def viewL(root):
    
    if not root :
        return [] 
    
    
    position = {} 
    
    queue = [(root,0)]
    max_level = 0
  
  
    
    while queue :
        
        node,level = queue.pop(0)
        if level not in position:
            position[level] = node.val
        
        max_level = max(max_level,level)
        
        
        if node.left :
            queue.append((node.left, level +1))
            
        if node.right :
            queue.append((node.right,level+1))
            
            
    return [position[level] for level in range (max_level + 1)]

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
    
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            node = queue.pop(0)
            
            # For left view, store the first node (i == 0)
            if i == 0:
                result.append(node.val)
            
            # Add children to queue
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return result

# Recursive Right/ Left View 


def Rview(root):
    
    res = [] 
    
    recursionR(root,0,res)
    
    return res 

def recursionR(root,level,res) :
    if not root :
        return 
    
    if len(res) == level :
        res.append(root.data)
        
    recursionR(root.right, level + 1, res)
        
    recursionR(root.left, level + 1, res)
    


def LView(root):
    
    result = [] 
    
    recursionL(root, 0, result)
    
    return result




def recursionL(root,level,res) :
    if not root :
        return 
    
    if len(res) == level :
        res.append(root.data)
        
    recursionR(root.left, level + 1, res)
        
    recursionR(root.right, level + 1, res)
        
    
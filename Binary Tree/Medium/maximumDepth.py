'''
LeetCode :> https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

'''
from queue import Queue


def maxi(root):
   
    if root is None :
        return 0 
    
    
    stack = Queue()
    counter = 0 
    
    stack.put(root)
    
    
    
    while not  stack.empty() : 
        level_size = stack.qsize()
       
        
        for _ in range (level_size):
            
            front = stack.get()
            
            if front.left is not None :
                stack.put(front.left)
                
            if front.right is not None :
                stack.put(front.right)
        counter += 1 
            
        
    return counter

# DFS Approach >> Optimal Code 

def maxiD(root):
    
    
    if not root :
        return 0 
    
    left_Depth = maxiD(root.left)
    right_Depth = maxiD(root.right)
    
    return 1 + maxiD(left_Depth,right_Depth)
    
    
    
    
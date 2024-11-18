'''
LeetCode :> https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

'''

from collections import deque


def zlevel(root):
    
    result = [] 
    
    if not root :
        return result 
    
    nodesQueue = deque([root]) 
    
    lefttoRight = True 
    
    while nodesQueue:
        
        size = len(nodesQueue)
        
        row = [0] * size 
        
        for i in range (size):
            node = nodesQueue.popleft() 
            
            index  = i if lefttoRight else (size -1 - i )
            
            
            row[index] = node.data 
            
            if node.left :
                nodesQueue.append(node.left)
                
            if node.right :
                nodesQueue.append(node.right)
                
                
        lefttoRight = not lefttoRight 
        
        result.append(row)
        
    return result
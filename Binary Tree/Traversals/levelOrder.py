'''
LeetCode :> https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000


'''

from collections import deque


def Order (root): 
    
    if not root :
        return []
    
    res = []    
    q = deque([root])
    
    while q :
        level_size = len(q)        
        current_level = []
        
        for _ in range  (level_size) : 
            
            node = q.popleft()
            
            current_level.append(node.val)
            
            if  node.left :
                q.append(node.left)
            
            if  node.right :
                q.append(node.right)
        
        res.append(current_level)
    
    return res
'''
LeetCode :> https://leetcode.com/problems/maximum-width-of-binary-tree/description/

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100

'''



from collections import deque

def widthOfBinaryTree(self, root):
    
    if not root:
        return 0
        
    # Queue will store tuples of (node, position)
    queue = deque([(root, 0,0)])
    max_width = 1
        
    while queue:
        # Your code here to process each level
        
        level_size = len(queue)
        first= last = 0
         
        # Think about:
        for i in range( level_size):
            # 1. How to get all nodes at current level
            node, id = queue.popleft()
            if i == 0 :
                first = id 
            last = id
        # 2. How to track leftmost and rightmost positions
            if node.left :
                queue.append((node.left,id * 2 ))
            if node.right :
                queue.append((node.right,id * 2 +1))
            
        # 3. How to calculate width
        max_width = max(max_width, last - first +1)
        
            
    return max_width


# Optimal Code 


def opwidth(root):
    
    if not root :
        return 0 
    
    maxW = 0 
    
    queue = deque([(root,0,0)])
    
    level_start = {}
    
    while queue :
        node,level,position = queue.popleft()
        
        if level not in level_start :
            level_start[level] = position 
            
        current_pos = position - level_start[level]
        maxW  = max(maxW, current_pos +1)
        
        if node.left :
            queue.append((node.left, level +1, current_pos * 2 ))
        
        if node.right : 
            queue.append((node.right, level+ 1, current_pos * 2 +1))
        
    return maxW
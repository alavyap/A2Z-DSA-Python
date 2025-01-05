'''
LeetCode :> https://leetcode.com/problems/count-complete-tree-nodes/description/

Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 6
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.


'''
# ‼️ not optimal 
def counT(root):
    
    if not root :
        return 0 
    counter = 0 
    
    if (root) and ((root.left or root.right) or (root.left is None or  root.right is None)):
        counter += 1 
    
    counter += counT(root.left)
    counter += counT(root.right)
    
    return counter


# Optimal Code 
def countN (root):
    
    if not root : 
        return 0 
    
    left_h = right_h = 0
    
    # Find left height 
    node = root
    while node.left :
        left_h += 1 
        node = node.left 
        
    # Find right height   
    node = root     
    while node.right :
        right_h += 1 
        node = node.right 
        
    if left_h  == right_h : 
        return (2 << (left_h)) -1 
    
    
    # if not perfect 
    return 1 + countN(root.left) + countN(root.right)
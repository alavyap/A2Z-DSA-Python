'''
LeetCode :> https://leetcode.com/problems/search-in-a-binary-search-tree/description/

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

 

Example 1:


Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]
Example 2:


Input: root = [4,2,7,1,3], val = 5
Output: []
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 107
root is a binary search tree.
1 <= val <= 107
'''
# Recursive Approach
def findVal(root,val):
    
    if not root :
       return None 
    
    if root.data == val :
        return root 
    
    if root.data < val:
      return findVal(root.right,val)
      
    if root.data > val :
        return findVal(root.left,val)
        
    
# Iterative Approach

def BSt(root,val):
    
    curr = root 
    while curr :
        
        if curr.val == val :
            return curr 
        elif curr.val < val :
            curr = curr.right 
        else :
            curr = curr.left 
    return None 


# Basic Logical Approach

def sBST(root,val):
    
    while root is not None and root.val != val :
        
        root = root.left if val < root.val else root.right 
    return root 
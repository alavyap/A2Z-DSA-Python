'''
LeetCode :> https://leetcode.com/problems/insert-into-a-binary-search-tree/description/


You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

 

Example 1:


Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
Explanation: Another accepted tree is: 5 as the root node and 4 is the right node of 3 

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]
Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]
 

Constraints:

The number of nodes in the tree will be in the range [0, 104].
-108 <= Node.val <= 108
All the values Node.val are unique.
-108 <= val <= 108
It's guaranteed that val does not exist in the original BST.


'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Approach
def insertVal(root,val):
    
    
    if root is None :
        return TreeNode(val)
        
    if (val > root.val):
        root.right = insertVal(root.right,val)
        
    else :
        root.left = insertVal(root.left,val)
        
    return root
    
    
    
# Iterative Approach

def insertinBST(root,val):
    
    if root is None :
        return TreeNode(val)  
    
    
    curr = root 
    
    while (root) :
        if (curr.val <= val): 
            
            if (curr.right != None) :
                curr = curr.right 
            else:
                curr.right  = TreeNode(val) 
                break
        else :
            if (curr.left != None) :
                curr = curr.left
            else :
                curr.left = TreeNode(val) 
                break 
            
    return root
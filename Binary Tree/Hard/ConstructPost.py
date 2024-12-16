'''
LeetCode :>  https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.

'''

def construct(inorder,postorder) :
    
    hashTree = {} 
    
    for i,val in enumerate(inorder):
        hashTree[val] = i 
        
    def builder(postStart,postEnd,inStart,inEnd):
        
        if (postStart > postEnd) or (inStart > inEnd):
            return None 
        
        root_val = postorder[postEnd]
        root = TreeNode(root_val)  #type: ignore
        
        inRoot = hashTree[root_val]
        
        numsleft = inRoot - inStart 
        
        
        root.left = builder(postStart ,postStart + numsleft -1, inStart,inRoot - 1)
         
        root.right = builder(postStart + numsleft ,postEnd -1  , inRoot + 1, inEnd)
        
        return root 
    
    return (builder(0,len(postorder)-1, 0 , len(inorder)-1)) 
         
        
                
                
                
                
# Not Optimal >> It is better for Space Complexity ,not on Time Complexity (O(N^2))
def notOptimal(inorder,postorder):
    
    def build(in_start,in_end,post_start,post_end):
        if in_start > in_end : 
            return None 
        
        root_val = postorder[post_end]
        root = TreeNode(root_val) #type:ignore
        
        inRoot = in_start
        while inorder[inRoot] != root_val: 
            inRoot += 1 
            
        numsleft = inRoot - in_start
        
        root.left = build(in_start, inRoot -1, post_start, post_start + numsleft -1) 
        root.right = build(inRoot +1, in_end,post_start + numsleft, post_end - 1)
        
        return root 
    return  build(0,len(inorder) -1, 0, len(postorder)-1)
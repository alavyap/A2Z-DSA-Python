'''
LeetCode :> https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]
 

Constraints:

1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder and inorder consist of unique values.
Each value of inorder also appears in preorder.
preorder is guaranteed to be the preorder traversal of the tree.
inorder is guaranteed to be the inorder traversal of the tree.


'''


def constructBT(preorder,inorder):
    
    hashTree = {} 
    
    for i,val in enumerate(inorder):
        hashTree[val] = i 
    
    def build (preStart,preEnd, inStart,inEnd):
        
        
        if (preStart > preEnd) or (inStart > inEnd):
            return None
        
        root_val = preorder[preStart]
        root = TreeNode(root_val) #type:ignore
        
        inRoot = hashTree[root_val]
        
        numsLeft = inRoot - inStart
        
        root.left = build(preStart +1, preStart +numsLeft, inStart, inRoot -1)
        root.right = build(preStart +numsLeft +1, preEnd, inRoot +1, inEnd)
        return root
        
    return (build(0, len(preorder)- 1 , 0, len(inorder) -1 ))


# Not Optimal >> It is better for Space Complexity ,not on Time Complexity (O(N^2))
def notOptimal(inorder,preorder):
    
    def builder(pre_start,pre_end,in_start,in_end):
        if in_start > in_end :
            return None 

        root_val = preorder[pre_start]
        root = TreeNode(root_val) #type:ignore
        
        inRoot = in_start
        
        while inorder[inRoot] != root_val :
            inRoot += 1 
        numleft = inRoot - in_start 
        
        root.left = builder(pre_start +1, pre_start + numleft,in_start, inRoot -1)
        root.right = builder(pre_start + numleft +1, pre_end, inRoot +1, in_end)
        
        return root 
    
    return (builder(0,len(preorder)-1, 0 ,len(inorder) -1))
        
        
        
    
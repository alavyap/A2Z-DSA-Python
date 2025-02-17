'''
Link :> https://www.lintcode.com/problem/448/

Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.

If the given node has no in-order successor in the tree, return null.

It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)

Example
Example 1:

Input: {1,#,2}, node with value 1
Output: 2
Explanation:
  1
   \
    2
Example 2:

Input: {2,1,3}, node with value 1
Output: 2
Explanation: 
    2
   / \
  1   3
Binary Tree Representation

Challenge
O(h), where h is the height of the BST.

'''

def bstIo(root,p):
    
    checker = None 
    
    while root  :
        if (p.val >= root.val):
            root = root.right
        else :
            checker = root
            root = root.left 
        
    return checker


'''
LeetCode :> https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/1436773247/

Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?

'''

# Code 1 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def preorderTraversal(self, root) :
        res = []
        def recursive(node):
            if not node :
                return 

            res.append(node.val)
            recursive(node.left)
            recursive(node.right)
        recursive(root)
        return res
    
# Code 2 
def preorderTraversal(self, root) :
        def preorder(node, res):
            if not node:
                return
            res.append(node.val)
            preorder(node.left, res)
            preorder(node.right, res)
        
        result = []
        preorder(root, result)
        return result


'''
Follow up: Recursive solution is trivial, could you do it iteratively?
'''

def itervative(root): 
    res = []
        
    if not root :
        return res
        
    stack = [root]
        
    while stack :
            
        curr = stack.pop() 
        res.append(curr.val)
            
            
        if curr.right :
            stack.append(curr.right)
        if curr.left :
            stack.append(curr.left)
    return res
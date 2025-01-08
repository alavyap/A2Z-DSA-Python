'''
LeetCode :> https://leetcode.com/problems/delete-node-in-a-bst/



Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:


Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.
Example 3:

Input: root = [], key = 0
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-105 <= Node.val <= 105
Each node has a unique value.
root is a valid binary search tree.
-105 <= key <= 105
 

Follow up: Could you solve it with time complexity O(height of tree)?


'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def deleteinBST(root,key):
    
    if not root :
        return None 
    
    if key < root.val :
        root.left = deleteinBST(root.left,key)
        
    elif key > root.val :
        root.right = deleteinBST(root.right,key)
        
    else :
        if not root.left and not  root.right :
            return None 
        if not root.left :
            return root.right 
        if not root.right :
            return root.left 
        
        root.val = findMin(root.right)
        root.right = deleteinBST(root.right,root.val)
    return root 

def findMin(root):
    while root.left :
        root = root.left 
    return root.val
'''

LeetCode :> https://leetcode.com/problems/balanced-binary-tree/description/

Given a binary tree, determine if it is 
height-balanced.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

'''

def isBalanced(root):
    
    if not root :
        return True 
    
    
    def getHeight(root):
        
        if not root :
            return 0
        
        leftDepth = getHeight(root.left)    
        rightDepth = getHeight(root.right)
        
        return 1 + max(leftDepth,rightDepth)    
        
        
        
    leftHeight = getHeight(root.left)
    rightHeight = getHeight(root.right)
    
    
    if abs(leftHeight - rightHeight) > 1 :
        return False

    return  isBalanced(root.left) and isBalanced(root.right)

    
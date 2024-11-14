'''
LeetCode :> https://leetcode.com/problems/diameter-of-binary-tree/description/

Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100

'''
# Brute Force 

def __init__ (self): 
    self.maxiD = 0

def dTree(root):
    
    if root is None :
        return 0
    
    leftH = dTree(root.left)
    rightH = dTree(root.right)
    
    maxiD = max(maxiD, leftH + rightH)
    
    return 1 + max(leftH,rightH)     

def diaTree(root):
    
    dTree(root)   
    return dTree.maxiD



# Optimal Approach 
def main(root):
    
    Dmeter = [0]    
    countH(root,Dmeter)    
    return countH.Dmeter[0] 


def countH(node,Dmeter):
    
    if not node :
        return 0 
    
    lh = countH(node.left,Dmeter)
    rh = countH(node.right,Dmeter)
    
    Dmeter[0] = max(Dmeter[0], lh + rh)
    
    return 1 + max(lh,rh)
    
    
    
    
'''
GFG :> https://www.geeksforgeeks.org/problems/minimum-element-in-bst/1

Given the root of a Binary Search Tree. The task is to find the minimum valued element in this given BST.

Examples

Input: root = [5, 4, 6, 3, N, N, 7, 1]
ex-1
Output: 1
Input: root = [10, 5, 20, 2]
ex-2
Output: 2
Input: root = [10, N, 10, N, 11]
             10
              \
               10
                \
                 11
Output: 10
Constraints:
0 <= number of nodes <= 105
0 <= node->data <= 105

'''

# Recursive Approach 

def miniVal(root):
    
    if not root :
        return None     
    if root.left :
        return miniVal(root.left)
    else :
        return root.data
       
    
    
# Iterative Appraoch 

def valueMin(root):

    if not root :
        return None     
    curr = root 
    while curr.left :
        curr = curr.left 
    return curr.data
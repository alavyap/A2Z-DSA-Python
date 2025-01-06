'''
LeetCode :> https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.


Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3 

Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104
 

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?


'''

# Brute Force 
def smallest(root,k):
    
    res = [] 
    
    def inOrder(node):
        if not node :
            return 
        inOrder(node.left)
        res.append(node.val)
        inOrder(node.right)
    inOrder(root)
    return res[k -1]


 
# Better Approach
def ksmallest(root,k):
    
    counter = 0 
    result = 0 
    
    def inOrder(node):
        nonlocal counter, result
        
        if not node :
            return False
        
        if inOrder(node.left):
            return True 
        
        counter += 1 
        if counter == k :
            result = node.val
            return True 
        
        return inOrder(node.right)
    
    inOrder(root)
    return result 
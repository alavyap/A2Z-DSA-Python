'''
LeetCode :> https://leetcode.com/problems/symmetric-tree/description/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
'''

# Recursive Solution 

def RTree(root):
    if not root :
        return True
    
    left = root.left 
    right = root.right
    
    def check(s1,s2):
        
        if not s1 and not s2 : 
            return True 
        
        if not s1 or not s2 :
            return False 
        
        return s1.val == s2.val and check(s1.left, s2.right) and check(s1.right , s2.left) 
    
    return check(left,right)

def ITree(root):
    if not root  :
        return True 
    
    queue = [(root.left,root.right )]
    
    while queue :
        left,right = queue.pop(0) 
        
        
        if not left and not right :
            continue 
        
        if not left or not right or left.val != right.val :
            return False 
        
        
        queue.append((left.left, right.right))
        queue.append((left.right,right.left))
        
    return True 
         
    
     
    
    
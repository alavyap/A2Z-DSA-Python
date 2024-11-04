'''
LeetCode :> https://leetcode.com/problems/binary-tree-postorder-traversal/description/

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
 
Follow up: Recursive solution is trivial, could you do it iteratively?


'''

def order(root):
    res = [] 
    
    def helper(rootNode):
        
        if not rootNode :
            return res
        
        helper(rootNode.left)
        helper(rootNode.right)
        res.append(rootNode.val)
        
    
    helper(root)
    return res

# 2 Stack Approach 

def stackOrder(root):
    
    res = [] 
    
    if not root :
        return res
    
    st1,st2 = [],[] 
    
    st1.append(root)
    
    while st1 :
        root = st1.pop() 
        
        st2.append(root)
        
        if root.left is not None :
            st1.append(root.left)
            
        if root.right is not None :
            st1.append(root.right)
            
            
    while st2 :
        res.append(st2[-1].val)
        st2.pop()
        
        
    return res


# Iterative Code L>R>Root


def Order(root):
    
    res = [] 
    
    if not root :
        return res 
    
    stack = [root]
    
    while stack  :
        
        curr = stack.pop() 
        res.append(curr.val) 
            
        if curr.left :
                stack.append(curr.left) 

        if curr.right :
            stack.append(curr.right)
        
        
    return res[::-1]
    
    

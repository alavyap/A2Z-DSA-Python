'''
LeetCode :> https://leetcode.com/problems/boundary-of-binary-tree/description/

Description
Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example
Example 1:

Input: {1,#,2,3,4}
Output: [1,3,4,2]
Explanation: 
  1
   \
    2
   / \
  3   4
  The root doesn't have left subtree, so the root itself is left boundary.
  The leaves are node 3 and 4.
  The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
  So order them in anti-clockwise without duplicates and we have [1,3,4,2].
Example 2:

Input: {1,2,3,4,5,6,#,#,#,7,8,9,10}
Output: [1,2,4,7,8,9,10,6,3]
Explanation: 
          1
     /          \
    2            3
   / \          / 
  4   5        6   
     / \      / \
    7   8    9  10  
  The left boundary are node 1,2,4. (4 is the left-most node according to definition)
  The leaves are node 4,7,8,9,10.
  The right boundary are node 1,3,6,10. (10 is the right-most node).
  So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].

'''

def bbTree(root):
    
    if not root :
        return [] 
    
    result = [] 
    
    def is_leaf(node):
        return node and not node.left and not node.right
    
    def add_left(node):
        if not node or is_leaf(node):
            return 
        
        result.append(node.val)
        if node.left:
            add_left(node.left)
        elif node.right :
            add_left(node.right)
            
            
    def add_leaves(node):
        if not node :
            return 
        if is_leaf(node):
            result.append(node.val)
            return 
        add_leaves(node.left) 
        add_leaves(node.right) 
        
    def add_right(node):
        if not node or is_leaf(node):
            return 
        result.append(node.val)
        
        if node.right:
            add_right(node.right)
        elif node.left :
            add_right(node.left)
            
        result.append(node.val)
        
        
    if not is_leaf(root):
        result.append(root.val)
        
    add_left(root.left)
    add_right(root.right)
    
    add_leaves(root)
    
    return result


# Faster Approach 

def isLeaf(root):
    
    return not root.left and not root.right

def addLeft(root,res) :
    
    curr = root.left 
    
    while curr :
        if not isLeaf(curr):
            res.append(curr.data)
            
        if curr.left :
            curr = curr.left
            
        else :
            curr = curr.right
            

def addRight(root,res):
    
    curr = root.right
    temp = [] 
    
    while curr :
        if not isLeaf(curr):
            temp.append(curr.data)
            
        if curr.right :
            curr = curr.right
        else :
            curr = curr.left
            
        for i in range (len(temp) -1,-1,-1):
            res.append(temp[i])
            
            
def addLeaves(root,res):
    
    if isLeaf(root):
        res.append(root.data)
        return
    
    if root.left :
        addLeaves(root.left,res)
    if root.right :
        addLeaves(root.right,res)
        
        
        
def main (root):
    res = [] 
    if not root :
        return res
    if not isLeaf(root):
        res.append(root.data)
        
    addLeft(root,res)
    addLeaves(root,res)
    addRight(root,res)
    
    return res


# Test Run 
print(main( [1,2,3,4,5,6,7,8,9,10]))
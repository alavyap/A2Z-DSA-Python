'''
Link :> https://leetcode.com/problems/recover-binary-search-tree/description/

You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Example 1:
Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

Example 2:
Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
 

Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
 
Follow up: A solution using O(n) space is pretty straight-forward. Could you devise a constant O(1) space solution?
'''

# O(N) << Space Complexity

def TreeR(root):
    
    inorder_nodes = [] 
    
    
    def inOrder_traversal(node):
        if not node : 
            return 
        
        inOrder_traversal(node.left)
        inorder_nodes.append(node)
        inOrder_traversal(node.right)
        
    inOrder_traversal(root)
    
    first = second = None 
    
    for i in range (len(inorder_nodes) -1 ):
        
        if inorder_nodes[i].val > inorder_nodes[i +1].val :
            second = inorder_nodes[i+1]
            if first is None :
                first = inorder_nodes[i]
            else :
                break 
            
    first.val, second.val = second.val, first.val        
        
    
    



# O(1) << Space Complexity Morris Law

def optimalTree(root):
    
    first = second = prev = None 
    curr = root 
    
    while curr :
        if not curr.left :
            if prev and prev.val > curr.val :
                if not first :
                    first = prev 
                second = curr 
            prev = curr 
            curr = curr.right 
            
        else :
            pred = curr.left 
            while pred.right and pred.right != curr :
                pred = pred.right
                
            if not pred.right :
                pred.right = curr 
                curr = curr.left 
                
            else :
                pred.right = None 
                
                
                if prev and prev.val > curr.val :
                    if not first :
                        first = prev 
                    second = curr 
                    
                prev = curr
                curr = curr.right
    first.val, second.val = second.val, first.val
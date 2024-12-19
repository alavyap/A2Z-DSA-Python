'''

DSA Sheet :> https://takeuforward.org/data-structure/morris-preorder-traversal-of-a-binary-tree/

Problem Statement: Given a Binary Tree, implement Morris Preorder Traversal and return the array containing its preorder sequence.

Morris Preorder Traversal is a tree traversal algorithm aiming to achieve a space complexity of O(1) without recursion or an external data structure. The algorithm should efficiently visit each node in the binary tree in preorder sequence, printing or processing the node values as it traverses, without using a stack or recursion

'''

def preOrder(root):
    
    preorder = [] 
    
    cur = root
    
    while cur is not  None :
        
        if cur.left is None :
            
            preorder.append(cur.val)
            cur = cur.right 
            
        else :
            
            prev = cur.left 
            while prev.right and prev.right != cur :
                prev = prev.right 
                
            if prev.right is None :
                prev.right = cur 
                
                cur = cur.left 
                
            else :
                prev.right = None 
                preorder.append(cur.val)
                cur = cur.right
    return preorder
            
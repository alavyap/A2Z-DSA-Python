'''

DSA Sheet :> https://takeuforward.org/data-structure/morris-inorder-traversal-of-a-binary-tree/

Problem Statement: Given a Binary Tree, implement Morris Inorder Traversal and return the array containing its inorder sequence.

Morris Inorder Traversal is a tree traversal algorithm aiming to achieve a space complexity of O(1) without recursion or an external data structure. The algorithm should efficiently visit each node in the binary tree in inorder sequence, printing or processing the node values as it traverses, without using a stack or recursion

'''

def inOrder(root):
    
    inorder = [] 
    
    cur = root 
    
    while cur is not None :
        
        if cur.left is None :
            inorder.append(cur.val)
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
                inorder.append(cur.val)
                cur = cur.right 
    return inorder
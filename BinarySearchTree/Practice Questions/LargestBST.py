'''
Link :> https://www.geeksforgeeks.org/problems/largest-bst/1


You're given a binary tree. Your task is to find the size of the largest subtree within this binary tree that also satisfies the properties of a Binary Search Tree (BST). The size of a subtree is defined as the number of nodes it contains.

Note: A subtree of the binary tree is considered a BST if for every node in that subtree, the left child is less than the node, and the right child is greater than the node, without any duplicate values in the subtree.

Examples :

Input: root = [5, 2, 4, 1, 3]
Output: 3
Explanation:The following sub-tree is a BST of size 3

Input: root = [6, 7, 3, N, 2, 2, 4]
Output: 3
Explanation: The following sub-tree is a BST of size 3:

Constraints:
1 ≤ number of nodes ≤ 105
1 ≤ node->data ≤ 105

'''

def largestBSTSubtree(self,root):
    if not root :
        return 0 
    
    if self.isBST(root,float("-inf"), float("inf")):
        return self.countNodes(root)
    return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))



def countNodes(self,node):
    if not node: 
        return 0 
    
    return 1 + self.countNodes(node.left) + self.countNodes(node.right)



def isBST(self,node,min_val,max_val):
    if not node:
        return True 
    
    if node.data <= min_val or node.data >= max_val:
        return False 
    
    return self.isBST(node.left,min_val,node.data) and self.isBST(node.right,node.data,max_val)



# Optimal Approach

def bst(self,root):
    def helper(node):
        if not node:
            return (True,0,float("inf"), float("-inf"))  #(isBST,size,min,max)
        
        left_isBST,left_size,left_min,left_max = helper(node.left)
        right_isBST,right_size,right_min,right_max = helper(node.right)
        
        
        # Check if the current subtree is BST
        if left_isBST and right_isBST and left_max< node.data < right_min :
            size = left_size + right_size + 1 
            return (True,size,min(node.data,left_min),max(node.data,right_max))
        else:
            return (False,max(left_size,right_size),0,0)
    return helper(root)[1]  
            
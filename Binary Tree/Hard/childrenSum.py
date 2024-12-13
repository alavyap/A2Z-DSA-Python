'''

GFG  :> https://www.geeksforgeeks.org/problems/children-sum-parent/1

Given a binary tree having n nodes. Check whether all of its nodes have a value equal to the sum of their child nodes. Return 1 if all the nodes in the tree satisfy the given properties, else it returns 0. For every node, the data value must be equal to the sum of the data values in the left and right children. Consider the data value 0 for a NULL child. Also, leaves are considered to follow the property.

Examples:

Input:
Binary tree
       35
      /  \
     20   15
    / \   / \
   15  5 10  5

Output: 1
Explanation: 
Here, every node is sum of its left and right child.
Input:
Binary tree
       1
     /   \
    4     3
   /  
  5    
Output: 0
Explanation: 
Here, 1 is the root node and 4, 3 are its child nodes. 4 + 3 = 7 which is not equal to the value of root node. Hence, this tree does not satisfy the given condition.
Input:
Binary tree
       10
      /  \
     4    6
    / \  / \
   1   3 2  4

Output: 1
Explanation: 
Here, every node is a sum of its left and right child.
Constraints:
1 <= number of nodes <= 105
0 <= node->data <= 105


'''


def isSum(root):
       
       def checker (node): 

              if not node : 
                     return True 
              
              if not node.left and not node.right :
                     return True 
              
              left_val = node.left.data if  node.left else 0 
              
              right_val = node.right.data  if node.right else 0
              
              return ((node.data == left_val + right_val) and              
                     checker(node.left) and 
                     checker(node.right)
              )
       return 1 if checker(root) else 0 
              
           
                     
              
       
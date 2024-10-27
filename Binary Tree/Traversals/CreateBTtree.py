'''
GFG > https://www.geeksforgeeks.org/problems/binary-tree-representation/1

You are given an array nodes. It contains 7 integers, which represents the value of nodes of the binary tree in level order traversal. You are also given a root of the tree which has a value equal to nodes[0].

Your task to construct a binary tree by creating nodes for the remaining 6 nodes.

Example:

Input: 
nodes = [1 2 3 4 5 6 7]
Output: 
         1
       /   \
     2       3
   /  \     /  \
   4  5    6   7
Explanation: 
The 7 node binary tree is represented above.
Your Task:

Complete the function void create_tree(node* root0, vector &vec), which takes a root of a Binary tree and vector array vec containing the values of nodes.

Expected Time Complexity: O(1).

Expected Auxiliary Space: O(1).

Constraints:

vec.length = 7

1<=vec[i]<=100
'''


from collections import deque


class Node :    
    def __init__(self,data):
        self.data= data 
        self.leftChild = None 
        self.rightChild = None
        
class Solution:
    def create(root,l):
        
        q = deque([root])
        
        i = 1 
        
        while i < len(l): 
            current = q.popleft()
            
            if i < len(l):
                current.left = Node(l[i])
                q.append(current.left)
                i += 1 
                
            if i < len(l) :
                current.right = Node (l[i])
                q.append(current.right)
                i += 1 
                
                
                
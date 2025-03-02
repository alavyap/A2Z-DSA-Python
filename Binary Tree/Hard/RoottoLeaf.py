'''
GFG :> https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1

Given a Binary Tree of nodes, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

Example 1:

Input:
       1
    /     \
   2       3
Output: 
1 2 
1 3 
Explanation: 
All possible paths:
1->2
1->3
Example 2:

Input:
         10
       /    \
      20    30
     /  \
    40   60
Output: 
10 20 40 
10 20 60 
10 30 
Your Task:
Your task is to complete the function Paths() which takes the root node as an argument and returns all the possible paths. (All the paths are printed in new lines by the driver's code.)

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(height of the tree)

Constraints:
1<=n<=104
'''

def path(root):
   
   all_paths = [] 
   current_path = [] 
   
   if not root :
      return [] 
   
   def dfs(node):
      
      current_path.append(node.data)
      
      
      if not node.left and not node.right :
         all_paths.append(current_path.copy())
         
      
      if node.left :
         dfs(node.left)
      
      if node.right :  
         dfs(node.right)
         
      
      current_path.pop()
   
   dfs(root)
   return all_paths
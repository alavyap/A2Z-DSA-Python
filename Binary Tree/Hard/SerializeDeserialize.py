'''

LeetCode :> https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/


Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000

'''
from collections import deque
from optparse import Values


def serialize(root) :
    
    if not root :
        return "#"
    
    s = []
    queue = deque([root])
    
    while queue:
        cur_node = queue.popleft() 
        
        if not cur_node :
            s.append("#")
        else : 
            s.append(str(cur_node.val))
            queue.append(cur_node.left)  
            queue.append(cur_node.right)
            
    while s and s[-1] == "#":
        s.pop()
        
    return ",".join(s) 


def deserialize(data): 
    
    if  data == "#" :
        return None 
    
    
    tokens = data.split(",")
    
    if not tokens :
        return None 
    
    root_val = tokens.pop(0)
    root = TreeNode(root_val) # type: ignore
    queue = deque([root])
    
    
    while  queue and tokens :
        
        node = queue.popleft()
        
        if tokens :
            left_val = tokens.pop(0)
            if left_val != "#":
                left_node = TreeNode(int(left_val)) # type: ignore
                node.left = left_node 
                queue.append(left_node)
                
        if tokens:        
            right_val = tokens.pop(0)
            if right_val != "#":
                right_node = TreeNode(int(right_val)) # type: ignore
                node.right = right_node
                queue.append(right_node)
                
    return root 
       
        
# Potential Optimal Code using DFS approach 

def serial(root):
    if not root :
        return "#"
    
    return f"{root.val},{serial(root.left)},{serial(root.right)}"


def deserial(data):
    
    def dfs() :
        val = next(values)
        
        if val == "#":
            return None 

        node = TreeNode(int(val)) # type: ignore
        
        node.left = dfs()
        node.right = dfs() 
        return node 
    values = iter(data.split(","))
    return dfs()
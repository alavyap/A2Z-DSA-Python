'''
Link :> https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

Example 1:

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105

'''
# Time and Space :> O(N) Approach 

def findTraget(root,k):
    
    def dfs(node,seen):
        if not node :
            return False 
        if k - node.val in seen:
            return True 
        seen.add(node.val)
        return dfs(node.left,seen) or dfs(node.right,seen) 
    return dfs(root,set())



# Using similar approach of TWO SUM Optimal Code {Expected in the interview}

def mainFunc(root,k):
    
    def pushLeft(stack,root):
        while root :
            stack.append(root)
            root = root.left
            
    def pushRight(stack,root):
        while root :
            stack.append(root)
            root = root.right 
            
    def moveLeft(stack):
        node = stack.pop() 
        pushLeft(stack,node.right)
        return node.val
    
    def moveRight(stack):
        node = stack.pop()
        pushRight(stack,node.left)
        return node.val
    
    stackLeft, stackRight = [], [] 
    pushLeft(stackLeft,root)
    pushRight(stackRight,root)
    
    left,right = moveLeft(stackLeft), moveRight(stackRight)
    while left < right :
        if left + right == k : return True 
        if left + right  < k :
            left = moveLeft(stackLeft)
        else: 
            right = moveRight(stackRight)
    return False
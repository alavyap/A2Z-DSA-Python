'''
GFG :> https://www.geeksforgeeks.org/problems/binary-search-trees/1

Given an array of integers arr[] representing inorder traversal of elements of a binary tree. Return true if the given inorder traversal can be of a valid Binary Search Tree.

Note - In a valid Binary Search Tree all keys are unique.

Examples :

Input: arr[] = [8, 14, 45, 64, 100]
Output: True
Input: arr[] = [5, 6, 1, 8, 7]
Output: False
Expected Time Complexity: O(n)

Expected Space Complexity: O(1)

Constraints:

1 <= n <= 105

1 <= arr[i] <= 109

'''

def checkBT(arr):
    
    if len(arr)  <= 1:
        return True 
    
    for i in range (1,len(arr)):
        if arr[i] <= arr[i-1]:
            return False 
    return True
    

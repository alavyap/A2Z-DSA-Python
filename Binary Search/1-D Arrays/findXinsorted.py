'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/binary-search_972
LeetCode :> https://leetcode.com/problems/binary-search/description/

Problem statement: You are given a sorted array of integers and a target, your task is to search for the target in the given array. 
Assume the given array does not contain any duplicate numbers.
Example:
Input: 'N' = 7 'target' = 3
'A' = [1, 3, 7, 9, 11, 12, 45]
Output: 1
Explanation: A = [1, 3, 7, 9, 11, 12, 45],
The index of element '3' is 1.
'''
# Iterative Implementation 
 
def binaryIter (arr,target):
    n = len(arr)
    low = 0 
    high = n-1
    while (low <= high):
        mid = (low +high ) //2 
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid +1
        
        else :
            high = mid - 1 
    return -1

# Test Run 
# print (binaryIter([1, 3, 7, 9, 11, 12, 45],3))


# Recursive Implementation 
def binaryRecu (arr,target):
    n = len(arr)
   
    return recursion(arr,0,n-1, target)
    
# Helper Function 
def recursion (arr,low,high,target):
    if low > high :
        return -1 
    mid = (low+ high)//2 
    if arr[mid] == target :
        return mid 
    elif target > arr[mid]:
        return recursion(arr,mid+1,high,target)
    return recursion (arr,low,mid-1,target)

# Test Run 
print (binaryRecu([1, 3, 7, 9, 11, 12, 45],3))
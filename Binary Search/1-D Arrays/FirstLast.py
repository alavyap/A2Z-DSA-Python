'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/first-and-last-position-of-an-element-in-sorted-array_1082549
LeetCode :> https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Problem Statement: Given a sorted array arr of n integers and a target value k. 
Write a program to find the indices of the first and the last occurrences of the target value. 
If the target is not found then return -1 as indices.
Note: Consider 0-based indexing.

Example :
Input Format: n = 8, arr[] = {2, 4, 6, 8, 8, 8, 11, 13}, k = 8
Result: 3 5
Explanation: The first occurrence of 8 is at index 3 and the last occurrence is at index 5.
'''

# Brute Force 
def brute (arr,k):
    n = len(arr)
    first = -1
    last = -1
    for i in range (n):
        if arr[i] == k:
            if first == -1 :
                first = i 
            last = i 
    return [first,last]

# Test Run 
print(brute([2, 4, 6, 8, 8, 8, 11, 13],8))

# Using 2 helper function 
def mainFunc(arr,k):
    n = len(arr)
    first = findFirst(arr,n,k)
    if first == n or arr[first] != k:
        return (-1, -1)
    last = findLast(arr,n,k)
    
    return [first,last-1]

# Helper Function 
def findFirst(arr,n,k):
    low = 0 
    high = n- 1
    ans = n 
    while (low <= high):
        mid = (low + high) // 2 
        
        if arr[mid] >= k :
            ans = mid 
            high = mid - 1 
        else :
            low = mid + 1 
    return ans 
     
def findLast(arr,n,k): 
    low = 0 
    high = n- 1
    ans = n 
    while (low <= high):
        mid = (low + high) // 2 
        
        if arr[mid] > k :
            ans = mid 
            high = mid - 1 
        else :
            low = mid + 1 
    return ans 

# Test Run 
# print(mainFunc([2, 4, 6, 8, 8, 8, 11, 13],8))
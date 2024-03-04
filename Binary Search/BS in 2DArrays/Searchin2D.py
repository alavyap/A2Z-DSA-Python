'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/search-in-a-2d-matrix_980531?leftPanelTabValue=PROBLEM
Leet Code :>  https://leetcode.com/problems/search-a-2d-matrix/

Problem Statement: You have been given a 2-D array ‘mat’ of size ‘N x M’ where ‘N’ and ‘M’ denote the number of rows and columns, respectively. 
The elements of each row are sorted in non-decreasing order. Moreover, the first element of a row is greater than the last element of the previous row (if it exists). 
You are given an integer ‘target’, and your task is to find if it exists in the given ‘mat’ or not.

Example :
Input Format: N = 3, M = 4, target = 8,
mat[] = 
1 2 3 4
5 6 7 8 
9 10 11 12
Result: true
Explanation: The ‘target’  = 8 exists in the 'mat' at index (1, 3).
'''
# Brute Force
def brute(arr,target):
    n = len(arr)
    m = len(arr[0])
    
    for i in range (n):
        for j in range (m):
            if arr[i][j] == target :
                return True 
    return False

# Test Run
# print(brute([[1,2,3,4],[5,6,7,8],[9,10,11,12]],69))

# Better Approach 
def better (arr,target):
    n = len(arr)
    m = len(arr[0])
    
    for i in range (n):
        if arr[i][0] <= target <= arr[i][m-1]:
            return higherBound(arr[i],target)
        
    return False

# Helper Function
def higherBound(arr,target):
    n = len(arr)
    low = 0 
    high = n- 1 
    
    while (low <= high): 
        
        mid =  (low + high) // 2 
        
        if arr[mid] == target :
            return True 
        
        elif (arr[mid] > target):
            high = mid -1 
        
        else :
            low = mid +1 
    return False         
# Test Run 
# print(better([[1,2,3,4],[5,6,7,8],[9,10,11,12]],9))

# Optimal Approach 
def optimal(arr,target):
    
    n = len(arr)
    m = len(arr[0])
    
    low = 0 
    high = (n *m ) -1 
    
    while (low <= high):
        mid = (low + high) // 2
        
        row = mid // m
        col = mid % m 
        
        if arr[row][col] == target:
            return  True 
        elif (arr[row][col] > target):
            high = mid - 1 
        else :
            low = mid + 1 
    return False

# Test Run 
print(optimal([[1,2,3,4],[5,6,7,8],[9,10,11,12]],9))
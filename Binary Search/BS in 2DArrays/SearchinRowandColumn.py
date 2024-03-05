'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/search-in-a-sorted-2d-matrix_6917532
LeetCode :> https://leetcode.com/problems/search-a-2d-matrix-ii/description/

Problem Statement: You have been given a 2-D array ‘mat’ of size ‘N x M’ where ‘N’ and ‘M’ denote the number of rows and columns, respectively. 
The elements of each row and each column are sorted in non-decreasing order.
But, the first element of a row is not necessarily greater than the last element of the previous row (if it exists).
You are given an integer ‘target’, and your task is to find if it exists in the given ‘mat’ or not.

Example :
Input Format: N = 3, M = 4, target = 3
mat[] = [ [1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60] ]

Result: true
Explanation: Target 3 is present in the cell (0, 1)(0-based indexing) of the matrix. So, the answer is true.

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
# print(brute([[1, 4, 7, 11, 15],
#     [2, 5, 8, 12, 19],
#     [3, 6, 9, 16, 22],
#     [10, 13, 14, 17, 24],
    # [18, 21, 23, 26, 30]],14))


# Better Approach 
def better(arr,target):
    n = len(arr)
    m = len(arr[0])
    
    for i in range (n):
        ans = helper(arr[i],target)
        if ans : 
            return True
        
    return False
    
    
# Helper
def helper(arr,target):
    low = arr[0] 
    n = len(arr)
    high = n- 1
    
    while (low <= high):
        mid = (low + high)// 2 
        if arr[mid] == target:
            return 1
        elif target < arr[mid]:
            high = mid -1 
        else :
            low = mid +1 
            
    return -1 



# Test Run 
# print(better([[1, 4, 7, 11, 15],
#     [2, 5, 8, 12, 19],
#     [3, 6, 9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]],14))



# Optimal Approach 
def optimal (arr,target):
    n = len(arr)
    m = len(arr[0])
    
    row = 0 
    col  = m -1
    
    # Traverse the matrix from (0,m-1)
    while (row < n and col >= 0 ):
        if arr[row][col] == target :
            return True 
        elif (arr[row][col] < target): 
            row += 1 
        else :
            col -= 1
    return False
   




# Test Run 
print(optimal([[1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]],14))
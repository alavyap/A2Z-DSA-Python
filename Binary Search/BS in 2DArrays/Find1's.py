'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/row-of-a-matrix-with-maximum-ones_982768

Find the row with maximum number of 1’s
Problem Statement: You have been given a non-empty grid ‘mat’ with ‘n’ rows and ‘m’ columns consisting of only 0s and 1s. All the rows are sorted in ascending order.
Your task is to find the index of the row with the maximum number of ones.
Note: If two rows have the same number of ones, consider the one with a smaller index. If there’s no row with at least 1 zero, return -1.

Example :
Input Format: n = 3, m = 3, 
mat[] = 
1 1 1
0 0 1
0 0 0
Result: 0
Explanation: The row with the maximum number of ones is 0 (0 - indexed).

'''
# Brute Force 
def brute (arr,n,m):
    cnt = 0 
    ans = -1 
    for i in range (n):
        cnt_ones = sum(arr[i])
        if cnt_ones > cnt :
            cnt = cnt_ones
            ans = i 
    return ans


# Test Run 
# print(brute([[1,1,1],[0,0,1],[0,0,0]],3,3))


# Optimal Approach 
def optimal(arr,n,m):
    cnt_max = 0 
    index = -1 
    
    for i in range (n):
        cnt_ones = m - lowerBound(arr[i],m,1)
        
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones 
            index = i 
    return index 

# Helper Function  > this can be done via lowerbound, higher bound and findelement way also 
def lowerBound(arr,n,target):
    low = 0 
    high = n-1
    ans  = n
    
    while (low <= high):
        mid = (low + high) // 2
        if arr[mid] >= target :
            ans = mid
            
            high = mid - 1
        else :
            low = mid +1 
    return ans 

# Test Run 
print(optimal([[1,1,1],[0,0,1],[0,0,0]],3,3))
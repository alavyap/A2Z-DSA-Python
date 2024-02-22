'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/rotated-array_1093219
LeetCode :> https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). 
Now the array is rotated between 1 to N times which is unknown. Find the minimum element in the array. 

Example :
Input Format: arr = [4,5,6,7,0,1,2,3]
Result: 0
Explanation: Here, the element 0 is the minimum element in the array.
'''
# Brute Force 
def brute (arr):
    n = len(arr)
    m = 0
    if n == 1 :
        return arr[0]
    for i in range (n):
        if arr[i] < arr[i-1]:
            m =  arr[i]
    return m
    
# Test Run 
# print(brute([4,5,6,7,0,1,2,3]))

# Optimal Approach 
def optimal(arr):
    n = len(arr)
    low = 0 
    high = n - 1 
    ans = float('inf')
    
    while (low <= high):
        mid = (low + high) // 2
        if arr[low]  <= arr[high] :
            ans = min(ans,arr[low])
            break
     
        if arr[low] <= arr[mid]:
            ans = min(ans,arr[low])
            low = mid +1 
            
        else :
            ans = min(ans,arr[mid])
            high = mid - 1 
            
    return ans
            
# Test Run 
print(optimal([4,5,6,7,0,1,2,3]))
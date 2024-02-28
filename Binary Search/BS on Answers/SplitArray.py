'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/largest-subarray-sum-minimized_7461751
LeetCode :> https://leetcode.com/problems/split-array-largest-sum/description/

Problem Statement: Given an integer array ‘A’ of size ‘N’ and an integer ‘K’.
Split the array ‘A’ into ‘K’ non-empty subarrays such that the largest sum of any subarray is minimized. Your task is to return the minimized largest sum of the split.
A subarray is a contiguous part of the array.

Example :
Input Format: N = 5, a[] = {1,2,3,4,5}, k = 3
Result: 6
Explanation: There are many ways to split the array a[] into k consecutive subarrays. 
The best way to do this is to split the array a[] into [1, 2, 3], [4], and [5], where the largest sum among the three subarrays is only 6.

'''
# Brute Force 
def brute (arr,k):
    n = len(arr)
    mini = max(arr)
    maxi = sum(arr)
    
    # Edge Case 
    if k > n :
        return -1
    
    for i in range (mini,maxi+1):
        if summation(arr,i) == k :
            return i 
    return mini

# Helper Function 
def summation(arr,pos):
    n = len(arr)
    totalP = 0 
    count = 1 
    for i in range (n):
        if totalP + arr[i] <= pos:
            totalP += arr[i] 
        else:
            count += 1 
            totalP = arr[i] 
            
    return count 

# Test Run 
# print(brute([1,2,3,4,5],3))

# Optimal Approach 
def optimal(arr,k):
    n = len(arr)
    
    # Edge Case 
    if k > n :
        return -1 
    
    low = max(arr)
    high = sum(arr)
   
    while (low <= high):
        mid = (low + high) //2 
        
        possi = helper(arr,mid)
        
        if possi > k :
            low = mid + 1 
        else: 
            high = mid - 1
            
    return  low 

# Helper Function 
def helper(arr,summ):
    n = len(arr)
    totalP = 0 
    count = 1
    for i in range (n):
        if totalP + arr[i] <= summ :
            totalP += arr[i] 
        else:
            count += 1 
            totalP = arr[i] 
            
    return count
        
        
# Test Run 
print(optimal([1,2,3,4,5],3))
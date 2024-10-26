'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/search-in-rotated-sorted-array_1082554
LeetCode :> https://leetcode.com/problems/search-in-rotated-sorted-array/

Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values) and a target value k. 
Now the array is rotated at some pivot point unknown to you. 
Find the index at which k is present and if k is not present return -1.

Example :
Input Format: arr = [4,5,6,7,0,1,2,3], k = 0
Result: 4
Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. 
Thus, we get output as 4, which is the index at which 0 is present in the array.

'''

# Brute Force 
def brute (arr,k):
    loc = -1
    n = len(arr) 
    for i in range (n):
        if arr[i] == k :
            loc = i 
    return loc

# Test Run 
# print(brute( [4,5,6,7,0,1,2,3],0))


# Optimal Approach 
def optimal (arr,k):
    n = len(arr)
    low = 0 
    ans = -1 
    high = n- 1
    while (low <= high):
        mid = (low +high) // 2
        if arr[mid] == k :
            ans = mid 
            
        if arr[low] <= arr[mid]:
            if arr[low] <=k and k <= arr[mid]:
                high = mid - 1 
            else :
                low = mid + 1 
        else :
            if arr[mid] <= k and k <= arr[high] :
                low = mid + 1 
            else :
                high = mid - 1
    return ans 


# Test Run 
print(optimal( [4,5,6,7,0,1,2,3],0))



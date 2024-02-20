'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/algorithm-to-find-best-insert-position-in-sorted-array_839813
LeetCode :> https://leetcode.com/problems/search-insert-position/description/

Problem Statement: You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array.
If the value is present in the array, then return its index. Otherwise, determine the index where it would be inserted in the array while maintaining the sorted order.

Example :
Input Format: arr[] = {1,2,4,7}, x = 6
Result: 3
Explanation: 6 is not present in the array. So, if we will insert 6 in the 3rd index(0-based indexing), the array will still be sorted. {1,2,4,6,7}.
'''

# Onlt way to solve
def brute (arr,x):
    n = len(arr)
    low = 0
    high = n - 1
    ans = n
    
    while (low <= high) :
        mid = (low + high) // 2 
        if arr[mid] >= x :
            ans = mid
            high = mid - 1 
            
        else  :
            low = mid +1 
    return ans 

# Test Run 
print(brute([1,2,4,7],6))
             
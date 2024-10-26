'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/kth-missing-element_893215
LeetCode :> https://leetcode.com/problems/kth-missing-positive-number/description/

Problem Statement: You are given a strictly increasing array ‘vec’ and a positive integer ‘k’. Find the ‘kth’ positive integer missing from ‘vec’.

Example :
Input Format: vec[]={4,7,9,10}, k = 1
Result: 1
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.
'''

# Brute Force 
def brute(arr, k):
    n = len(arr)
    for i in range (n):
        if arr[i] <= k :
            k += 1 
        else :
            break
    return k

# Test Run 
# print(brute([4,7,9,10],1))

# Optimal Approach 
def optimal (arr,k):
    n = len(arr)
    low = 0 
    high = n-1 
    
    while(low <= high):
        mid = (low + high) //2 
        miss = arr[mid] - (mid+1)
        
        if (miss <k ):
            low = mid +1 
        else:
            high = mid - 1 
    return (high+ 1 + k)

# Test Run 
print(optimal([4,7,9,10],5))

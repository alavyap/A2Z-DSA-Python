'''
Link :> https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_6682399?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems
Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.
Example :
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.
Sliding Window Technique Question >> That to of variable window 
Because  the lenght of window is not defined but the sum of the window should be of K which is given. 
'''

# Brute Force 
from operator import length_hint


def longestsubArray(arr,k):
    n = len(arr)
    length = 0
    for i in range (n):
        sum = 0 
        for j in range (i,n):
            sum += arr[j]
        
            if sum == k :
                length = max(length,j-i+1)

    return length

# Test Run
print(longestsubArray([1, 2, 3, 1, 1, 1, 1],3))








# Optimal Approach
# def longestSubarray(arr,k):
    
    
    
    
    
    
# Test Run
# print(longestSubarray([1, 2, 3, 1, 1, 1, 1],3))
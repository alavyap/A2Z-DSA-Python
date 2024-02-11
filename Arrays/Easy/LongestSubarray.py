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
# print(longestsubArray([1, 2, 3, 1, 1, 1, 1],3))



# Optimal Approach  >This is a sliding window problem but the platforms would not accept is so doing just as arrays

def longestSubarray(arr,k):
    n = len(arr)
    right,left = 0,0
    Sum = arr[0]
    maxLen = 0
    while right < n :
        while left <= right and Sum > k:
            Sum -= arr[left]
            left += 1
        
        if Sum == k :
            maxLen = max(maxLen, right-left + 1)
            
        right += 1
        if right < n :
            Sum += arr[right]         
    return maxLen
    
    
    

    
# Test Run
# print(longestSubarray([1, 2, 3, 1, 1, 1, 1],3))

# LeetCode 
def subarraySum(nums,k):
    Sum = 0 
    preSum = 0
    storeSum = {0:1}
    
    for i in nums :
        preSum = preSum + i
        
        if (preSum - k) in storeSum :
            Sum = Sum + storeSum[preSum - k] 
            
        if preSum not in storeSum :
            storeSum[preSum] = 1
            
        else:
            storeSum[preSum] = storeSum[preSum] + 1
    return Sum

# Test Run 
print(subarraySum([1, 2, 3, 1, 1, 1, 1],3))

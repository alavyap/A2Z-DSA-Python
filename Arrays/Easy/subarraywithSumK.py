'''
Link :> https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_5713505?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems
Problem Statement: Given an array and a sum k, we need to print the length of the longest subarray that sums to k.
Example
Input Format: N = 3, k = 5, array[] = {2,3,5}
Result: 2
Explanation: The longest subarray with sum 5 is {2, 3}. And its length is 2.
THis contains both Positives and Negatives in the array
'''

# Brute Force 
def getLongestSubarray(nums,k):
    n = len(nums)
    for i in range (n):
        sum = 0
        for j in  range (i,n):
            sum += nums[j]
        
        if sum == k :
            length = j-i+1
            
    return length



# Optimal Approach 
def LongestSubarray(nums,k):
    n = len(nums)
    preSum = {}
    Sum = 0
    maxLength = 0
    for i in range (n):
        
        Sum += nums[i]
        
        if Sum == k :
            maxLength = max(maxLength, i+1)
            
        rem = Sum - k
        
        if rem in preSum :
            length = i - preSum[rem]
            maxLength = max(maxLength, length)
            
        if Sum not in preSum :
            preSum[Sum] = i
            
    return maxLength
           
# Test Run 
# print(getLongestSubarray([1,2,1,0,1],4))
print(LongestSubarray([1,2,1,0,1],4))



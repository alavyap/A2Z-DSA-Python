'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/maximum-subarray-sum_630526?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode :> https://leetcode.com/problems/maximum-subarray/description/
Kadane's Algorithm : Maximum Subarray Sum in an Array
Problem Statement: Given an integer array arr, find the contiguous subarray (containing at least one number) which
has the largest sum and returns its sum and prints the subarray.

Examples
Example 1:

Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 

Output: 6 

Explanation: [4,-1,2,1] has the largest sum = 6. 
'''
def kaden(arr):
    n = len(arr)
    max = 0
    for i in range (n):
        sum = 0 
        for j in range (i+1,n):
            sum += arr[j]
            
        if max < sum :
            max = sum 
    return max
    
# Test Run 
print (kaden([-2,1,-3,4,-1,2,1,-5,4] ))
'''
LeetCode :> https://leetcode.com/problems/sum-of-subarray-minimums/description/


Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104

'''

# Brute Force 
from turtle import right


def minSum(arr):
    n = len(arr)
    sumSub  =0 
    MOD = 10 ** 9 + 7
    
    for i in range (n):
        for j in range (i,n):
            sumSub += min(arr[i:j+1])
            
    sumSub = (sumSub % MOD)
    return sumSub


# Optimal Approach 
def subMin(arr):
    
    n= len(arr)
    MOD = 10 ** 9 + 7
    
    stack = [] 
    right = [n] * n 
    left = [-1] * n
    
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i] :
            right[stack.pop()] = i 
        stack.append(i)
        
    stack.clear()
    
    
    
    for i in range (n-1,-1,-1):
        while stack and arr[stack[-1]] >= arr[i] :
            left[stack.pop()] = i 
        stack.append(i)
        
    result = 0 
    
    for i in range(n):
        result += arr[i] * (i - left[i]) * (right[i] - i )
        result %= MOD 
    return result
            
 
a = [3,1,2,4]

print(minSum(a))
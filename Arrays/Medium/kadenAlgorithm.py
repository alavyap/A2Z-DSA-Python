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


# Brute Force
def largestSum(arr):
    n = len(arr)
    max1 = 0
    for i in range (n):
        sum = 0 
        for j in range (i,n):
            sum += arr[j]
            
            max1 = max(max1,sum)
    return max1
    
# Test Run 
# print (largestSum([-2,1,-3,4,-1,2,1,-5,4]))



# Optimal Approach
def kadenAlgo (nums):
    n = len(nums)
    # If the question is asking to return negative sum, in a negative array then we use  Max = float('-inf')
    
    Max = Sum = 0 
    # Max = float('inf')
    for i in range (n):
        Sum += nums[i]
        
        if Sum > Max :
            Max = Sum 
            
        if Sum < 0:
            Sum = 0 
            
    return Max

# Test Run
# print (kadenAlgo([-2,1,-3,4,-1,2,1,-5,4]))


'''
Follow Up :  > 
There might be more than one subarray with the maximum sum. We need to print any of them.
'''

def folloUp (arr):
    n = len(arr)
    ansStart = ansEnd = -1
    maxi = total = 0 
    for i in range (n):
        
        if total == 0 :
            start = i   #starting index
            
        total += arr[i] 
        
        if total > maxi :
            maxi = total
            
            # we set the location for the subarray 
            ansStart = start 
            ansEnd = i
            
        if total < 0 : 
            total = 0
            
            
    # To print the subarray
    for element in range (ansStart,ansEnd+1):
        print (arr[element],end= ", ")
    
    
# Test Run 
folloUp([-2,1,-3,4,-1,2,1,-5,4])

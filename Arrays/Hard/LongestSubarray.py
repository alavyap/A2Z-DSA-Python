'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/longest-subarray-with-zero-sum_6783450?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf


Problem Statement: Given an array containing both positive and negative integers, 
we have to find the length of the longest subarray with the sum of all elements equal to zero.

Example :
Input Format: N = 6, array[] = {9, -3, 3, -1, 6, -5}
Result: 5
Explanation: The following subarrays sum to zero:
{-3, 3} , {-1, 6, -5}, {-3, 3, -1, 6, -5}
Since we require the length of the longest subarray, our answer is 5!
'''

# Brute Force 
def longestBF(arr):
    n = len(arr)
    maxi = 0 
   
    for i in range (n):
        sum = 0 
        for j in range (i,n):
            sum += arr[j] 

            if sum == 0 :
                maxi = max(maxi, j -i+1)
    return maxi
    
     
# Test Run 
# print (longestBF([9,-3,3,-1,6,-5]))

# Optimal Approach 
def longestOA(arr):
    n = len(arr)
    maxi = 0 
    sum = 0
    store = {}
    for i in range (n):
        sum += arr[i] 
        
        if sum == 0 :
            maxi = i+1 
        else :
            if sum in store :
                maxi = max(maxi,i-store[sum])
                
            else :
                store[sum] = i 
                
    return maxi
    
# Test Run  
print (longestOA([9,-3,3,-1,6,-5]))
 
   
 
 
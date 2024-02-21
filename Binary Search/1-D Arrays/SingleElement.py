'''
Coding Ninja :>  https://www.codingninjas.com/studio/problems/unique-element-in-sorted-array_1112654
LeetCode :> https://leetcode.com/problems/single-element-in-a-sorted-array/description/

Problem Statement: Given an array of N integers. Every number in the array except one appears twice. 
Find the single number in the array.

Example :
Input Format: arr[] = {1,1,2,2,3,3,4,5,5,6,6}
Result: 4
Explanation: Only the number 4 appears once in the array.
'''
# Brute Force 
def brute (arr):
    n = len(arr)
    if n == 1 :
        return arr[0]
    for i in range (n):
        
        if i == 0 :
            if arr[i] != arr[i+1] :
                return arr[i] 
        elif i == n- 1 :
            if arr[i] != arr[i-1] :
                return arr[i] 
        else :
            if arr[i] !=  arr[i-1] and arr[i] != arr[i+1] :
                return arr[i]
    return -1

# Test Run 
print(brute([1,1,2,2,3,3,4,5,5,6,6]))
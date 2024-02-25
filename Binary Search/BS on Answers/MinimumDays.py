'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/rose-garden_2248080
LeetCode :>  https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description/

Problem Statement: You are given ‘N’ roses and you are also given an array ‘arr’  where ‘arr[i]’  denotes that the ‘ith’ rose will bloom on the ‘arr[i]th’ day.
You can only pick already bloomed roses that are adjacent to make a bouquet. You are also told that you require exactly ‘k’ adjacent bloomed roses to make a single bouquet.
Find the minimum number of days required to make at least ‘m’ bouquets each containing ‘k’ roses. Return -1 if it is not possible.

Example :
Input Format: N = 8, arr[] = {7, 7, 7, 7, 13, 11, 12, 7}, m = 2, k = 3
Result: 12
Explanation: On the 12th the first 4 flowers and the last 3 flowers would have already bloomed.
So, we can easily make 2 bouquets, one with the first 3 and another with the last 3 flowers.
'''
# Brute Force 
from math import floor


def brute(arr,r,b):
    n = len(arr)
    totalF = r * b 
    maxi = funcMax(arr,n)
    mini = funcMin(arr,n)
    
    # Edge Case 
    if  n  < totalF :
        return -1
    
    # return maxi,mini
    for i in range (mini, maxi+1):
        if possible(arr,r,b,n,i):
            return i 
    return -1
    


    
    
# Function to find the max element in the array 
def funcMax(arr,n):
    maxi = float('-inf')
    
    for i in range (n) :
        if maxi < arr[i] :
            maxi = arr[i] 
            
    return maxi 
    
# Function to find the min element in the array 
def funcMin(arr,n):
    mini = float('inf')
    
    for i in range (n) :
        if mini > arr[i] :
            mini = arr[i] 
            
    return mini 

# This function is to find the possible boquets 
def possible (arr,r,b,n,day):
    cnt = 0 
    noOf = 0
    for i in range (n):
        if arr[i] <= day :
            cnt += 1
        else: 
            noOf += (cnt // b)
            cnt = 0
    noOf += cnt // b
    return noOf >= r
# Test Run 
print(brute([7,7,7,7,13,11,12,7],2,3))
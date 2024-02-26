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

def brute(arr,r,b):
    n = len(arr)
    totalF = r * b
    
    # Edge Case 
    if  n  < totalF :
        return -1
    maxi = float('-inf') 
    mini = float('inf')
    for i in range (n):
        maxi = max(maxi,arr[i])
        mini = min(mini,arr[i])
    
    # return maxi,mini
    for i in range (mini, maxi+1):
        if possible(arr,r,b,i):
            return i 
    return -1
    
# This function is to find the possible boquets 
def possible (arr,r,b,day):
    n = len(arr)
    cnt = 0 
    noOf = 0
    for i in range (n):
        if arr[i] <= day :
            cnt += 1
        else: 
            noOf += (cnt // r)
            cnt = 0
    noOf += cnt // r
    return noOf >= b


# Test Run 
# print(brute([7,7,7,7,13,11,12,7],2,3))


# Optimal Approach 

def optimal (arr,m,k):
    n = len(arr)
    totalP = m * k
    
    if n < totalP :
        return -1 
    
    low = float('inf')
    high = float('-inf')
    
    for i in range (n):
        low = min(low,arr[i])
        high = max(high,arr[i])
        
    while (low <= high):
        mid = (low + high) // 2 
        
        if possible (arr,m,k,mid) :
            high = mid -1 
        else :
            low = mid + 1
        
    return low 

# Helper Function 
def possible(arr,m,k,day):
    n = len(arr)
    cnt = 0 
    noOf = 0 
    for i in  range (n):
        if arr[i] <= day :
            cnt += 1 
        else :
            noOf += cnt // k
            cnt = 0 
    noOf += cnt // k 
    return noOf >= m

# Test Run 
print(optimal([7,7,7,7,13,11,12,7],2,3))
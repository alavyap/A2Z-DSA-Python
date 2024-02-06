'''
Problem Statement: Given an array of N integers, your task is to find unique triplets that add up to give a sum of zero. In short,
you need to return an array of all the unique triplets [arr[a], arr[b], arr[c]] such that i!=j, j!=k, k!=i, and their sum is equal to zero.
Example : 
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k
'''
# Brute Force 
def sum3(arr):
    n = len(arr)
    ans = []
    temp = []
    inSet = set()
    for i in range (n):
        for j in range (i+1,n):
            for k in range (j+1,n):
                if arr[i] + arr[j] +arr[k] == 0:
                   temp = [arr[i],arr[j],arr[k]]
                   temp.sort()
                   inSet.add(tuple(temp))
    
    ans = [list(items) for items in inSet]
    return ans
# Test Run 
# print (sum3( [-1,0,1,2,-1,-4]))


# Better Approach 

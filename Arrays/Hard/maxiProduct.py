'''
Coding Ninja : > https://www.codingninjas.com/studio/problems/subarray-with-maximum-product_6890008?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode :> https://leetcode.com/problems/maximum-product-subarray/description/

Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.
Example :
Input: Nums = [1,2,-3,0,-4,-5]
Output: 20
Explanation:  In the given array, we can see (-4)*(-5) gives maximum product value.
'''
#  Subarray means contigous elements 

# Brute Force 
def bf (arr):
    n = len(arr)
    maxi = 0 
    pro = 1
    for i in range (n):
        for j in range (i+1,n):
            pro = arr[i] *arr[j]
            
        if maxi < pro :
            maxi = pro
    return maxi

# Test Run 
# print(bf([1,2,-3,0,-4,-5]))
print(bf([1,-2,3,-4]))
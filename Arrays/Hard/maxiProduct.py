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
    maxi = arr[0]
    for i in range (n-1):
        pro = arr[i]
        for j in range (i+1,n):
            maxi = max(maxi,pro)
            pro *= arr[j]
        if maxi < pro :
            maxi = pro
    return maxi

# Test Run 
# print(bf([1,2,-3,0,-4,-5]))
# print(bf([1,-2,3,-4]))

# Optimal Approach >> this better solution 
def op(arr):
    n = len(arr)
    prefix = 1 
    suffix = 1
    result = float('-inf') 
    for i in range (n):
        if prefix == 0 :
            prefix = 1 
        if suffix ==  0 :
            suffix = 1 
        prefix *= arr[i] 
        suffix *= arr[n-i-1]
        
        result = max(result , max(prefix,suffix))
    return result

# Test Run 
# print(op ([1,2,-3,0,-4,-5]))



# Kadens Algorithm 

def kadenOP(arr):
    n = len(arr)
    pro1 = arr[0] 
    pro2 = arr[0] 
    ans = arr[0] 
    
    for i in range (1,n):
        temp = max(arr[i],pro1 * arr[i], pro2* arr[i])
        
        pro2 = min (arr[i], pro1 *arr[i], pro2 * arr[i])
        
        pro1 = temp 
        
        ans = max(ans,pro1)
        
    return ans


# Test Run 
print(kadenOP ([1,2,-3,0,-4,-5]))

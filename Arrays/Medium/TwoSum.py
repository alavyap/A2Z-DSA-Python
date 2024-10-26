'''
Problem Statement: Given an array of integers arr[] and an integer target.

1st variant: Return YES if there exist two numbers such that their sum is equal to the target. Otherwise, return NO.
2nd variant: Return indices of the two numbers such that their sum is equal to the target. Otherwise, we will return {-1, -1}.

Note: You are not allowed to use the same element twice. Example: If the target is equal to 6 and num[1] = 3, then nums[1] + nums[1] = target is not a solution.

Example :
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
Result: YES (for 1st variant)
       [1, 3] (for 2nd variant)
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

'''
# Brute Force
# 1st Variant
def twoSum (arr,k):
    n = len(arr)
    for i in range  (n):
        for j in range (i+1,n):
            sum = arr[i] + arr[j]
            if sum == k :
                return "Yes"
    return "No"
            
# 2nd Variant 
def two_sum(arr,k):
    n = len(arr)
    for i in range (n):
        for j in range (i+1,n):
            sum = arr[i] +arr[j] 
            if sum == k :
                return [i,j]
    return [-1,-1]
# TestRun
# print(twoSum([2,6,5,8,11],14))
# print(two_sum([2,6,5,8,11],14))


# Better Approach
def TwoSum (arr,k):
    n = len(arr)
    store = {}
    for i in range (n):
        if arr[i] in store :
            store[arr[i]] += 1
        else :
            store[arr[i]] = 1
             
        sum = k -arr[i] 
    #     if sum in store.keys():
    #         return "Yes"
    # return "NO"
    
    
    # 2nd Variant 
        if sum in store :
            return [store[sum],i]
    return [-1,-1]  

# Test Run 
# print(TwoSum([2,6,5,8,11],14))


# Optimized Approach 
def TwosuM (arr,k):
    n = len(arr)
    # Sorting the array > is required if it is just asking YES or NO
    # for i in range (n):
    #     for j in range (i+1,n):
    #         if arr[i] >arr[j]:
    #             arr[i],arr[j] = arr[j],arr[i]
                
    arr.sort()
    # two sum 
    l = 0 
    r = n -1
    while (l <r):
    #     sum = arr[l] +arr[r]
    #     if sum == k :
    #         return "Yes"
    #     elif (sum < k):
    #         l += 1
    #     else :
    #         r -= 1
    # return "No"
    
    # 2nd Varient 
            sum = arr[l] + arr[r]
            if sum == k:
                return [l,r]
            elif (sum < k):
                l += 1
            else:
                r -= 1
    return [-1,-1]

    
    

# Test Run          
# print(TwosuM([2,6,5,8,11],14))
# print(TwosuM([3,2,4],6))




'''
Excellent Solution this is able to solve both the variants of the question  on Coding NInja and LeetCode
'''
# Time Cpmplexity >> O(N)
# Space Complexity >> O(N)

def correctTwoSum (arr,k):
    n = len(arr)
    store = {}
    for el in range (n):
        remain = k - arr[el]
        if remain in store :
            return [store[remain],el]
        store[arr[el]] = el
    return []

# Test Run
print (correctTwoSum([3,2,4],6))


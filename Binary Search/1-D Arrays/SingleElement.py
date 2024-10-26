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
# print(brute([1,1,2,2,3,3,4,5,5,6,6]))

# Brute Force Type 2 

def bruteT(arr):
    n = len(arr)
    ans = 0 
    for i in range (n):
        ans = ans ^ arr[i] 
    return ans 

# Test Run 
# print(bruteT([1,1,2,2,3,3,4,5,5,6,6]))


# Optimal Approach 
def optimal(arr):
    n = len(arr)
    
    low = 1 
    high = n-2 
    
    # Edge Case 
    if n == 1 :
        return arr[0] 
    
    if arr[0] != arr[1]:
        return arr[0] 
    
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    while (low <= high):
        mid = (low + high) // 2 
        
        if arr[mid] != arr[mid -1] and arr[mid] != arr[mid +1 ]:
            return arr[mid]
        
        if (mid % 2 == 0 and arr[mid] == arr[mid+1]) or (mid %2 == 1 and arr[mid] == arr[mid -1 ]) :
            low  = mid + 1 
        else :
            high = mid -1 
            
    # Dummy Case 
    return -1
    
# Test Run 
print(optimal([1,1,2,2,3,3,4,5,5,6,6]))

            
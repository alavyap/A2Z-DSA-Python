'''
Cooding Ninja :> https://www.codingninjas.com/studio/problems/find-peak-element_1081482
LeetCode :>  https://leetcode.com/problems/find-peak-element/description/

Problem Statement: Given an array of length N. Peak element is defined as the element greater than both of its neighbors.
Formally, if 'arr[i]' is the peak element, 'arr[i - 1]' < 'arr[i]' and 'arr[i + 1]' < 'arr[i]'. 
Find the index(0-based) of a peak element in the array. If there are multiple peak numbers, return the index of any peak number.

Note: For the first element, the previous element should be considered as negative infinity as well as for the last element, 
the next element should be considered as negative infinity.

Example :
Input Format: arr[] = {1,2,3,4,5,6,7,8,5,1}
Result: 7
Explanation: In this example, there is only 1 peak that is at index 7.

'''
# Brute Force 

def brute (arr):
    n = len(arr)
    if n == 1 :
        return 0 
    
    for i in range (n):
        if i == n-1 :
            if arr[n-1] > arr[n-2] :
                return n-1
        if i == 0 :
            if arr[0] > arr[1] :
                return i 
        else :
            if arr[i] > arr[n-1] and arr[i] > arr[i +1]:
                return i 
            
    
# Test Run 
# print (brute([1,2,3,4,5,6,7,8,5,1]))

# Brute Force 
def bruteT (arr):
    n = len(arr)
    for i in range (n):
        if (i == 0 or arr[i] >arr[i-1]) and (i == n-1 or arr[i] > arr[i+1]):
            return i 
    return -1
  
# Test Run 
# print (bruteT([1,2,3,4,5,6,7,8,5,1]))


# Optimal  Approach 

def optimal(arr):
    n = len(arr)
    
    # Base Case 
    if n == 1 :
        return 0 
    
    if arr[0] > arr[1]:
        return 0 
    if arr[n-1] > arr[n-2]:
        return n- 1
    
    
    low = 1 
    high = n-2
    
    while (low <= high)  :
        mid = (low + high) // 2 
        
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid +1]:
            return mid 
        
        if arr[mid] >arr[mid-1]:
            low = mid +1 
        else :
            high = mid - 1
            
    return -1     
# Test Run 
print (optimal([1,2,3,4,5,6,7,8,5,1]))
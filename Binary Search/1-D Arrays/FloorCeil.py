'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/ceiling-in-a-sorted-array_1825401

Problem Statement: You're given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1].
The floor of x is the largest element in the array which is smaller than or equal to x.
The ceiling of x is the smallest element in the array greater than or equal to x.

Example :
Input Format: n = 6, arr[] ={3, 4, 4, 7, 8, 10}, x= 5
Result: 4 7
Explanation: The floor of 5 in the array is 4, and the ceiling of 5 in the array is 7.
'''

# Solution 
def mainFunc (arr,x):
    n = len(arr)
    floor = findFloor (arr,n,x)
    ceil = findCeil(arr,n,x)
    
    return floor, ceil


# Finding Floor 
def findFloor(arr,n,x):
    low =0 
    high = n- 1
    ans = -1 
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] <= x :
            ans = arr[mid]
            low = mid + 1 
        else :
            high = mid - 1 
    return ans 

# Finding Ceil 
def findCeil(arr,n,x):
    low = 0 
    high = n- 1 
    ans = -1 
    while (low <= high):
        mid = (low + high) //2 
        if arr[mid] >= x :
            ans = arr[mid]
            high = mid - 1
            
        else :
            low = mid + 1 
    return ans 


# Test Run 
print (mainFunc([3, 4, 4, 7, 8, 10],5))
            
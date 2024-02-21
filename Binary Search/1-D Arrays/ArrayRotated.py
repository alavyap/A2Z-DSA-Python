'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/rotation_7449070
  
Problem Statement: Given an integer array arr of size N, sorted in ascending order (with distinct values). 
Now the array is rotated between 1 to N times which is unknown. Find how many times the array has been rotated. 

Example :
Input Format: arr = [4,5,6,7,0,1,2,3]
Result: 4
Explanation: The original array should be [0,1,2,3,4,5,6,7]. So, we can notice that the array has been rotated 4 times.

'''
# Brute Force 
def brute (arr):
    n = len(arr)
    ans = float('inf')
    index = -1 
    for i in range (n):
        if arr[i] < ans :
            ans = arr[i] 
            index = i 
        return index


# Test Run 
# print(brute([4,5,6,7,0,1,2,3]))

# Optimal Apprach 
def optimal (arr):
    n = len(arr)
    low = 0 
    high = n -1 
    ans = float('inf')
    index = -1
    
    while (low <= high):
        mid = (low + high) // 2
        
        
        if arr[low] <= arr[high] :
                
            if arr[low] < ans :
                ans = arr[low]
                index = low 
            break
        
         
        if arr[low] <= arr[mid]:
            if arr[low]  < ans : 
                ans = arr[low]
                index = low
            low = mid + 1 
        else :
            if arr[mid] < ans :
                ans =arr[mid]
                index =mid
            high = mid - 1 
            
    return index 

# Test Run 
print(optimal([4,5,6,7,0,1,2,3]))

# Important Question 
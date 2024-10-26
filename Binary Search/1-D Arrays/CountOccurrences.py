'''
Coding Ninja :> 
Problem Statement: You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.
Example :
Input: N = 7,  X = 3 , array[] = {2, 2 , 3 , 3 , 3 , 3 , 4}
Output: 4
Explanation: 3 is occurring 4 times in 
the given array so it is our answer.
'''

# Brute Force 
def brute (arr,k):
    count = 0 
    for i in range (len(arr)):
        if arr[i] == k :
            count += 1 
    return count

# Test Run 
# print(brute([2, 2 , 3 , 3 , 3 , 3 , 4],3))

# Optimal Approach 
def mainFunc(arr,k):
    n = len(arr)
    first,last = firstAndLast(arr,n,k)    
    if first == - 1 :
        return 0 
    return last - first +1 

def firstAndLast(arr,n,k):
    first = firstCount (arr,n,k)
    if first == -1 :
        return (-1,-1)
    last = lastCount(arr,n,k)
    return (first,last)

def firstCount(arr,n,k):
    low = 0 
    high = n -1 
    first = - 1 
    while (low <= high) :
        mid = (low +high) // 2
        if arr[mid] == k :
            first = mid 
            high = mid -1 
        elif arr[mid] < k :
            low = mid + 1
        else:
            high = mid - 1 
            
    return first 

def lastCount (arr,n,k):
    low = 0 
    high = n- 1 
    last = - 1 
    while (low <= high):
        mid = (low + high) // 2 
        if arr[mid] == k :
            last = mid 
            low = mid +  1 
        elif arr[mid] < k :
            low = mid + 1 
        else :
            high = mid - 1 
    return last

# Test Run 
print(mainFunc([2, 2 , 3 , 3 , 3 , 3 , 4],3))
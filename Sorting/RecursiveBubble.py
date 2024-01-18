'''
Problem Statement: Given an array of N integers, write a program to implement the Recursive Bubble Sort algorithm.
Examples:

Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52
'''


def recursiveBubble(arr,n):
    # n = len(arr)
    if n == 1: 
        return 
    for i in range (n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
            
    recursiveBubble(arr,n-1)
    return arr


# Test Run 
print(recursiveBubble([13,46,24,52,20,9],6))



# Optmizied Bubble Sort 
def optrecuriseBubble(arr,n):
    if n == 1 :
        return
    
    swapped = False
    
    for i in range (n-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1], arr[i]
            swapped = True
    if not swapped :
        return        
    
    optrecuriseBubble(arr,n-1)
    return arr


# Test Run 
print(optrecuriseBubble([13,46,24,52,20,9],6))
'''
Problem Statement: Given an array of N integers, write a program to implement the Recursive Insertion Sort algorithm.
Example:

Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52
'''

def recursiveInsertion(arr,n):
    if n <= 1 :
        return 
    
    key = arr[n-1]
    j = n- 2
    
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1 
    arr[j+1] = key
    
    recursiveInsertion(arr,n-1)
    return arr

# Test Run

print(recursiveInsertion([13,46,24,52,20,9],6))
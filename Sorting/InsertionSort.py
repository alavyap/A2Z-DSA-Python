'''
Given an array of N integers, write a program to implement the Insertion sorting algorithm.
Example:

Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9,13,20,24,46,52
'''

def insertionSort(arr):          #Time and Space Complexity >>  O(n^2) {O(n) if the array is already sorted} &O(1)
    n = len(arr)                
    for i in range (1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
    return arr
 

# TestRun
print(insertionSort([13,46,24,52,20,9]))

# Optimized Version of the above > there is a other called binary insertion sort
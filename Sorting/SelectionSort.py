'''
Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.

Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting the array is: 9, 13, 20, 24, 46, 52


'''

def selectionSort (arr):                              #Time and Space Complexity >> O(n^2) and O(1)
    n = len(arr)
    for i in range (n-1):
        min_index = i
        for j in range (i+1,n):
            if arr[min_index] > arr[j] :
                min_index = j
                # Swap the found minimum element with the first element
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


print(selectionSort([13,46,24,52,20,9]))


'''
Coding Ninja :- Sort the given unsorted array 'arr' of size 'N' in non-decreasing order using the selection sort algorithm.


'''

def selectionSort(arr):         #Time and Space Complexity >> O(n^2) & O(1)
    n = len(arr)
    for i in range (n-1):
        min_index = i
        for j in range (i+1,n):
            if arr[min_index] > arr[j]:
                min_index = j
                
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
            
    return arr

# Test Run
print(selectionSort([8, 6, 2, 5, 1]))
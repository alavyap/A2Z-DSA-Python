'''
Problem Statement:  Given an array of n integers, sort the array using the Quicksort method.
Example:

Input:  N = 5  , Arr[] = {4,1,7,9,3}
Output: 1 3 4 7 9 
Explanation: After sorting the array becomes 1, 3, 4, 7, 9
'''
def quickSortWrapper(arr):              #This will take the array
    quickSort(arr,0,len(arr)-1)
    return arr

def quickSort(arr,low,high):
    if low < high:
        pivotIndex = partition(arr,low,high)
        quickSort(arr,low,pivotIndex-1)
        quickSort(arr,pivotIndex+1,high)
        
        
# Helper Function 
def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    
    while i < j :
        while i <= high - 1 and arr[i] <= pivot :
            i += 1
        while j >= low + 1 and arr[j] > pivot:
            j -= 1
            
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[low],arr[j] = arr[j],arr[low]
    return j
    


# Test Run 
print(quickSortWrapper([4,1,7,9,3]))


def quick_sort(arr):    #Using List Comprehension
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)
# print("Sorted array:", sorted_arr)



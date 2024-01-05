'''
Merge Sort Time Complexity is O(NLogN) and Space Complexity is O(N)
Problem:  Given an array of size n, sort the array using Merge Sort.
Example:

Input: N=5, arr[]={4,2,1,6,7}
Output: 1,2,4,6,7
'''

def mergeSort(arr):             #This is the main function in the merge sort as it takes the array
    if len(arr) > 1 :
        
        mid = len(arr) //2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursive calls to sort the left and right halves 
        mergeSort(left_half)
        mergeSort(right_half)
        
        # Merge the sorted left and right halves
        mergeHelper (arr, left_half, right_half)
    return arr

def mergeHelper(arr,left,right):              #This is the helper function that divides and merge the array in the merge sort
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        
    # Handle remaining in the left half
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    # Handle remaining in the right half
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        
        
# Test Run
print (mergeSort([4,2,1,6,7]))



'''
Coding Ninja >> Doing this with single function instead of 2 Functions
'''

def singleMergeSort(arr):
    if len(arr) > 1 :
        mid = len(arr) //2
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        # Recursive call to sort the left and the right halves
        singleMergeSort(left_half)
        singleMergeSort(right_half)
        
        
        i = j = k = 0
        
        # Merge the left and right halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            
        # Sorting the left half 
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            
        # Sorting the right half 
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
    
# Test Run 
print(singleMergeSort([2, 13, 4, 1, 3, 6, 28]))



# When l and r is given 

def Merge(arr,l,m,r):
    n1 = m - l + 1
    n2 = r - m 
    
    L = [0] * (n1)
    R = [0] * (n2)
    
    for i in range (0,n1):
        L[i] = arr[l+i]
        
    for j in range (0, n2):
        R[j] = arr[m + 1+ j]
        
    i = 0 
    j = 0
    k = l
    
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j] 
            j += 1
        k += 1
        
    # Sorting the left Side 
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Sorting the Right Side 
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
    
    
def cnMerge(arr, l, r):
    
    if l < r :
        m = (l+(r-1)) //2
        cnMerge(arr,l,m)
        cnMerge(arr,m+1,r)
        Merge(arr,l,m,r)
    return arr

# Test Run 
arr = [2, 13, 4, 1, 3, 6, 28]
print (cnMerge(arr,0,6))
    
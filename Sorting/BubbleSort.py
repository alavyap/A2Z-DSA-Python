
'''
Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.
Examples:

Input: N = 6, array[] = {13,46,24,52,20,9}
Output: 9,13,20,24,46,52
Explanation: After sorting we get 9,13,20,24,46,52
'''
def bubbleSort(arr):
    # My Approach 
    # for i in range (len(arr)):
    #     for j in range (i+1,len(arr)):
    #         if arr[i] > arr[j]:
    #             arr[i],arr[j]=arr[j],arr[i]  
    '''
    So the above code will check till the end even if the element is sorted in the first iteration 
    Where as in the below code the number of iterations will keep decreasing as the last element get sorted 
    '''
    
    for i in range (len(arr)-1):
        for j in range (len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                           
    return arr

# Test Run 
print(bubbleSort([13,46,24,52,20,9]))


# Optimized approach (Reducing time complexity for the best case):

'''
Coding Ninja
'''
def optimizedBubbleSort(arr):
    n = len(arr)
    for i in range (n-1):
        swapped = False
        for j in range (n-i - 1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True                    
                    
        if not swapped:
            break
        
    return arr

# TestRun 
print (optimizedBubbleSort([99,67,58,3,12]))



'''
Link :  https://takeuforward.org/data-structure/union-of-two-sorted-arrays/

Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
The union of two arrays can be defined as the common and distinct elements in the two arrays.

**Note : Elements in the union should be in ascending order.

Example:
Input:
n = 5,m = 5.
arr1[] = {1,2,3,4,5}  
arr2[] = {2,3,4,4,5}
Output:{1,2,3,4,5}
'''

def unionArray(arr1,arr2):   #Brute Force 
    n = len(arr1)
    m = len(arr2)
    union = set()
    
    for i in range (n):
        union.add(arr1[i])
    for j in range (m) :
        union.add(arr2[j]) 
        
    return union


# Test Run 
# print(unionArray( [1, 2, 3, 4, 6],[2, 3, 5]))

# Optimized Approach
def mergeArrays(a,b):
    n = len(a)  #length of the arrray a
    m = len(b) #length of the array b
    
    i,j = 0,0  #the pointer for the both the arrays 
    union = [] # the new array that will store the union of both the arrays 
    
    
    while i < n and j < m :  #the is the main loop which is checking if the pointer are with in the range of both the arrays length
        if a[i] <= b[j] :  # this condition is checking if the element in a is less then or equal to element in array b
            if  len(union)  == 0 or union[-1] != a[i] : # this condition is checking if the union array is empty if True OR  
                # the second is checking if the last element of the union array is not equal to the current element of the array
                union.append(a[i])
            i += 1
            
        else :
            # the below codintion is checking either union is empty or the last element of union is not equal to current element of b, either is true it will execute the below code 
            if len(union) == 0 or union[-1] != b[j] :   
                
                union.append(b[j])
            j += 1
            
            
    # this condintion will check if there is any left element in the array a 
    while i < n :
        if union[-1] != a[i] :
            union.append(a[i]) 
        i += 1
    
    # This will check if there is any element left in array b
    while j < m :
        if union[-1] != b[j] :
            union.append(b[j])
        j += 1
    
    return union

# Test Run
print(mergeArrays([1, 2, 3, 4, 6],[2, 3, 5]))
                
    
    
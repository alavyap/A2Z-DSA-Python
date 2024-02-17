'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/number-of-inversions_6840276?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_Arrayproblems

Problem Statement: Given an array of N integers, count the inversion of the array (using merge-sort).
What is an inversion of an array? 
Definition: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].

Example :
Input Format: N = 5, array[] = {5,4,3,2,1}
Result: 10
Explanation: we have a reverse sorted array and we will get the maximum inversions as for i < j we will always find a pair such that A[j] < A[i]. 
Example: 5 has index 0 and 3 has index 2 now (5,3) pair is inversion as 0 < 2 and 5 > 3 which will satisfy out conditions and 
for reverse sorted array we will get maximum inversions and that is (n)*(n-1) / 2.
For above given array there is 4 + 3 + 2 + 1 = 10 inversions.
'''

# Brute Force 


def bf (arr):
    n = len(arr)
    count = 0
    for i in range (n):
        for j in range (i+1,n):
            if arr[i] > arr[j] :
                count += 1 
    return count 

# Test Run 
# print(bf([5, 3, 2, 1, 4]))

# Optimal Approach >> Using Merge Sort 
def op(arr):
    n = len(arr)
    
    return merger(arr,0,n-1)

# Helper Function
def merger( arr,low,high):
    count = 0 
    if low >= high :
        return count 
    
    mid = ((low + high) // 2)
    
    count += merger(arr,low,mid)
    count += merger(arr,mid +1, high)
    count += mergeSort (arr,low,mid,high)
    return count 
     
def mergeSort (arr,low,mid,high):
    temp = [] 
    left = low 
    right = mid + 1 
    count = 0 
    
    while (left <=  mid and right <= high):
        if (arr[left] <= arr[right]):
            temp.append(arr[left])
            left += 1 
        else : 
            temp.append(arr[right])
            count += (mid - left +1)
            right += 1 
        
    # If Elements are on the left half still in the left     
    while (left <= mid): 
        temp.append(arr[left])
        left += 1 
        
    # If elements are on the right half of the array 
    while (right <= high):
        temp.append(arr[right])
        right += 1 
        
    # transferring all the elements from temporary to arr 
    for i in range (low,high + 1):
        arr[i] = temp[i -low]
    return count 

 
# Test Run 
print(op([5, 3, 2, 1, 4]))
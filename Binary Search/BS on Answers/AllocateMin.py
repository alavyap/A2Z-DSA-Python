'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/allocate-books_1090540

Problem Statement: Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book. There are a ‘m’ number of students, 
and the task is to allocate all the books to the students.
Allocate books in such a way that:

1. Each student gets at least one book.
2. Each book should be allocated to only one student.
3. Book allocation should be in a contiguous manner.
You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum. 
If the allocation of books is not possible. return -1

Example :
Input Format: n = 4, m = 2, arr[] = {12, 34, 67, 90}
Result: 113
Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

'''
# Brute Force 
def brute(arr,m):
    n = len(arr)
    mini  = max(arr)
    maxi = sum(arr)
    
    # Edge Case 
    if m > n :
        return -1
    
    for i in range (mini,maxi+1):
        if helper(arr,i) == m :
            return i
    return mini
        
# Helper Function 
def helper(arr,pages):
    n = len(arr)
    student = 1 
    totalP = 0 
    for i in range (n):
        if totalP + arr[i] <= pages:
            totalP += arr[i]
        else :
            student +=1 
            totalP = arr[i] 
            
    return student          

# Test Run 
# print(brute([12, 34, 67, 90],2))

# Optimal Approach 
def optimal (arr,m):
    n = len(arr)
    low = max(arr)
    high = sum(arr)
    
    if m > n :
        return -1 
    
    while (low <= high):
        mid = (low + high) // 2 
        
        # if help(arr,mid) == m :
        #     return mid 
        
        if  help (arr,mid) > m :
            low = mid + 1 
        else :
            high = mid - 1 
            
    return low 

# Helper Function 
def help(arr,pages):
    n= len(arr)
    student = 1 
    totalP = 0 
    
    for i in range (n):
        if totalP + arr[i] <= pages :
            totalP += arr[i]  
        else: 
            student += 1
            totalP = arr[i]
            
    return student

# Test Run 
print(optimal([12, 34, 67, 90],2))
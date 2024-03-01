'''
Coding Ninja : > https://www.codingninjas.com/studio/problems/median-of-two-sorted-arrays_985294
LeetCode :> https://leetcode.com/problems/median-of-two-sorted-arrays/description/

Problem Statement: Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays. 
The median is defined as the middle value of a sorted list of numbers. 
In case the length of the list is even, the median is the average of the two middle elements.

Example :
Input Format: n1 = 3, arr1[] = {2,4,6}, n2 = 3, arr2[] = {1,3,5}
Result: 3.5
Explanation: The array after merging 'a' and 'b' will be { 1, 2, 3, 4, 5, 6 }. As the length of the merged list is even, the median is the average of the two middle elements. 
Here two medians are 3 and 4. So the median will be the average of 3 and 4, which is 3.5.

'''

# Brute Force 

def brute(arr1,arr2):
    n = len(arr1)
    m = len(arr2)
    
    arr3 = [] * (n+m)
    i = 0
    j = 0
    
    while (i <n and j < m):
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j+= 1
            
    # Left Over Elements in the Array of both
    while (i < n):
        arr3.append(arr1[i])
        i+= 1
        
    while (j < m):
        arr3.append(arr1[j])
        j+= 1
        
    l = len(arr3)
    if l %2 == 1 :
        return float (arr3[l //2])
     
    ans = (arr3[l//2] + arr3[(l //2) -1] ) / 2.0
    return ans
    
# Test Run 
# print(brute([2,4,6],[1,3]))


# Better Approach
def better(a,b):
    n = len(a)
    m = len(b)
    cnt = 0 
    l = n +m
    ind2 = (l) //2 
    ind1 = (ind2 ) -1
    ind1El = -1  
    ind2El = -1  
    
    i = 0 
    j = 0 
    
    while (i <n and j < m):
        if a[i] < b[j]:
            if cnt == ind1 :
               ind1El = a[i]
               
            if cnt == ind2 :
                ind2El = a[i] 
            cnt += 1
            i += 1
        else :
            if cnt == ind1 :
                ind1El = b[j] 
            if cnt == ind2 :
                ind2El = b[j] 
            cnt += 1
            j += 1
            
            
    # For Left Over 
    while (i <n):
        if cnt == ind1 :
            ind1El = a[i] 
        if cnt == ind2: 
            ind2El = a[i] 
        cnt += 1 
        i += 1 
    
    while (j <m):
        if cnt == ind1 :
            ind1El = b[j] 
        if cnt == ind2 :
            ind2El = b[j] 
            
        cnt += 1
        j += 1 
        
    
    # Finding the Median 
    if l % 2 == 1 : 
        return float(ind2El)   
    
    return float(ind1El + ind2El) / 2.0


# Test Run 
# print(better([2,4,6],[]))


# Optimal Approach 

def optimal(a,b):
    n = len(a)
    m = len(b)
    
    if n > m :
        return optimal(b,a)
    
    l = n + m 
    left = (n + m + 1 ) // 2 
    
    # Applying Binary Search 
    low, high = 0 , n 
    
    while (low <=  high):
        mid1 = (low + high) // 2 
        mid2 = left - mid1 
        
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        
        if mid1 < n :
            r1 = a[mid1]
        if mid2 < m :
            r2 = b[mid2]
        if mid1 - 1 >= 0  :
            l1 = a[mid1 - 1]
        if mid2 -1 >= 0 :
            l2 = b[mid2 -1]
            
            
        if l1 <= r2  and l2 <= r1 :
            if l % 2 == 1 :
                return float(max(l1,l2))
            else :
                return (float(max(l1,l2)) + float(min(r1,r2))) / 2.0

        # Eliminate the halves 
        elif l1 > r2 :
            high = mid1 -1 
        else:
            low = mid1 +1 
    return 0


# Test Run 
print(optimal([1, 3, 5, 7], [2, 4, 6, 8]))





















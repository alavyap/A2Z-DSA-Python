'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/k-th-element-of-2-sorted-array_1164159

Problem Statement: Given two sorted arrays of size m and n respectively, you are tasked with finding the element that would be at the kth position of the final sorted array.
Input: m = 5
       n = 4
       array1 = [2,3,6,7,9]
       array2 = [1,4,8,10]
       k = 5
Output: 6
Explanation: Merging both arrays and sorted. Final array will be -
 [1,2,3,4,6,7,8,9,10]
We can see at k = 5 in the final array has 6. 
'''
# Brute Force 
def brute (a,b,k ):
    n = len(a)
    m = len(b)
    merger = [] 
   
    
    i = 0 
    j = 0 
    
    while (i <n and j < m):
        if a[i] <b[j]:
            merger.append(a[i])
            i += 1
        else :
            merger.append(b[j])
            j += 1
            
            
    # For the remaining element [left overs ]
    while (i <n):
        merger.append(a[i])
        i += 1 
    while (j <m):
        merger.append(b[j])
        j += 1
    
    # Output 
    if k >= len(merger):
        return -1
    return merger[k-1]

# Test Run 
# print(brute([2,3,6,7,9],[1,4,8,10],5))

# Better Approach
def better(a,b,n,m,k):
   
    # Intial Values 
    p1 = 0  # this will work with first array 
    p2 = 0  #this will work with second array 
    counter = 0
    ans = 0 
    
    # using merge sort algo 
    while (p1 <m and p2 <n):
        if (counter == k ):
            break
        elif (a[p1] < b[p2]):
            ans = a[p1]
            p1 += 1 
            
        else:
            ans = b[p2]
            p2 += 1 
            
        counter += 1 
        
    if (counter != k):
        if (p1 != m-1):
            ans = a[k- counter]
        else :
            ans = b[k-counter]
    return ans 

# Test Run 
# print(better([2,3,6,7,9],[1,4,8,10],4,5,5))


# Optimal Approach 
def optimal(a,b,n,m,k):
    
    # Edge Case 
    if m > n :
        a,b,m,n = b,a,n,m
        # Also the length 
               
    low = max(0,k-m)
    high = min(k,n)
    
    while (low <= high):
    
        cut1 = (low + high) // 2
        cut2 = k - cut1 
        
        l1 = float('-inf') if cut1 == 0 else  a[cut1 -1]
        l2 = float('-inf') if cut2 == 0 else b[cut2 -1]
        
        r1 = float('inf') if cut1 == n else a[cut1]
        r2 = float('inf') if cut2 == m else b[cut2]
        
        if l1 <= r2 and l2 <= r1 :
            return max(l1,l2)
    
        elif l1 > r2 :
            high = cut1 -1 
    
        else:
            low = cut1 + 1
    
    return -1 
    
# Test Run 
print(optimal([2,3,6,7,9],[1,4,8,10],4,5,5))
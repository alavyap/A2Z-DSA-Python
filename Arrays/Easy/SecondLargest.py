'''
Link > https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse

Problem statement
You have been given an array 'a' of 'n' unique non-negative integers.
Find the second largest and second smallest element from the array.
Return the two elements (second largest and second smallest) as another array of size 2.

Example :
Input: 'n' = 5, 'a' = [1, 2, 3, 4, 5]
Output: [4, 2]
The second largest element after 5 is 4, and the second smallest element after 1 is 2.
'''
# Brute Force  >> This will only work if there is no duplicate values 
'''
def getSecond(a,n):
    for i in range (n):
        for j in range( i+1, n):
            if a[i] > a[j]:
                a[i],a[j] = a[j],a[i]
        
    return (a[1],a[n-2])
'''

# Better Approach
'''
def getSecond (a,n):
    if n == 0 or n == 1 :
        return (-1,-1)
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_largest = float('-inf')
    
    for i in range (n):
        small = min(small,a[i]) 
        large = max(large,a[i])
        
    for i in range (n):
        if a[i] < second_small and a[i] != small:
            second_small = a[i]
            
        if a[i] > second_largest and a[i] != large :
            second_largest =  a[i]
            
    return (second_small, second_largest)
'''

# Optimal Approach
import re


def getSecond(a,n):
    print(secondSmall(a,n))
    print(secondLarge(a,n))
    

def secondSmall(a,n):
    small = float('inf')
    second_small = float('inf')
    if n < 2 :
        return (-1)
    for i in range (n):
        if a[i] < small:
            second_small = small 
            small = a[i]
        elif a[i] <second_small and a[i] != small :
            second_small = a[i] 
    return second_small 

def secondLarge(a,n):
    large = float('-inf')
    second_large = float('-inf')
    if n <2 :
        return -1
    
    for i in range (n):
        if a[i] > large:
            second_large = large 
            large = a[i]
        if a[i] > second_large and a[i] != large :
            second_large = a[i] 
    return second_large 

# Test Run
print(getSecond([1, 2, 3, 4, 5],5))
# print(secondSmall([1, 2, 3, 4, 5],5))
# print(secondLarge([1, 2, 3, 4, 5],5))
# print(getSecond([1, 2, 4, 6, 7, 5],5))
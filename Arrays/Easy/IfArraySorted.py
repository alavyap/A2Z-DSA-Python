'''
Link > https://www.codingninjas.com/studio/problems/ninja-and-the-sorted-check_6581957?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse
Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. 
If the array is sorted then return True, Else return False.

Sample Input 1 :
4
0 0 0 1
Sample Output 1 :
1
Explanation For Sample Input 1 :
The given array is sorted in non-decreasing order; hence the answer will be 1. 
'''



from turtle import Turtle


def isSorted(n,a):              #Brute Force
    if n == 0 or n == 1 :
        return 
    
    for i in range (n):
        for j in range (i+1,n):
            if a[i] > a[j]:
                return 0
    return True
            
            
def optisSorted(a, n):
    if n == 0 or n == 1:
        return 

    for i in range(1, n):
        if a[i] < a[i - 1]:
            return 0

    return 1

# Test Run 
print(optisSorted(3, [1,2,3]))


# LeetCOde

def check(nums):
    count  = 0 
    for i in range (len(nums)):
        if nums[i] < nums[i-1]:
            count += 1
    
    if count <= 1 :
        return True
    else:
        return False
    


# Test Run
print(check([1,2,3]))
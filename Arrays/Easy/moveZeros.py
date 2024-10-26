'''
Problem :  You are given an array of integers, your task is to move all the zeros in the array to the end of the array and
move non-negative integers to the front by maintaining their order

Example :
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order


'''

import re
from shutil import move


def moveZero(arr):   #Brute Force 
    n = len(arr)
    for i in range (n-1):
        for j in range (i+1,n):
            if arr[i] == 0 :
                arr[i],arr[j] = arr[j],arr[i]      
    return arr


# Test Run 
# print(moveZero([ 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]))
    
    
# Optimal Approach

def moveZeros(arr):
    n = len(arr)
    zero = 0 
    for index in range (n):
        if arr[index]  != 0  and arr[zero] == 0:
            arr[zero],arr[index] = arr[index], arr[zero]
            
        if arr[zero] != 0:
            zero += 1
    return arr



# Test Run 
print(moveZeros([ 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]))
    
    
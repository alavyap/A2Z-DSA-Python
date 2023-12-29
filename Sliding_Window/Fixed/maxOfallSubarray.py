'''
Given an array arr[] of size N and an integer K. Find the maximum for each and every contiguous subarray of size K.

Example:
Input 1:
    A = [1, 3, -1, -3, 5, 3, 6, 7]
    B = 3
Output 1:
    C = [3, 3, 5, 5, 6, 7] . 
'''

from unittest import result


def maxSub_Array(a,b):
    
    # this take the length of the array
    N = len(a)
    
    # this stores the max of a window
    result = []

          
          
# Test Run 
print(maxSub_Array([1,3,-1,-3,5,3,6,7],3))  
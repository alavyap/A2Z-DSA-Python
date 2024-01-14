'''
Link: https://takeuforward.org/data-structure/linear-search-in-c/
Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.
Example:

Input: arr[]= 1 2 3 4 5, num = 3
Output: 2
Explanation: 3 is present in the 2nd index
'''

def linearSearch(arr, num):
    for i in range (len(arr)):
        if arr[i] == num :
            return (i)
    return -1   

# Test Run 
print(linearSearch([6,7,8,4,1],4))
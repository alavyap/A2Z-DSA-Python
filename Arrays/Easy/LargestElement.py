'''
Link > https://www.codingninjas.com/studio/problems/largest-element-in-the-array-largest-element-in-the-array_5026279?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse
Problem statement
Given an array 'arr' of size 'n' find the largest element in the array.

Example:
Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]
Output: 5
Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.
'''

def largestElement(arr,n):
    if n == 0 or n == 1 :
        return
    max = arr[0]
    for i in range (1,n):
        if arr[i] > max:
            max = arr[i]
    return max

# Test Run
print(largestElement([19,2,3,4,5],5)) 
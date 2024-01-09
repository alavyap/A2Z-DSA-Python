'''
Link > https://www.codingninjas.com/studio/problems/left-rotate-an-array-by-one_5026278?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse

Problem statement
Given an array 'arr' containing 'n' elements, rotate this array left once and return it.
Rotating the array left by one means shifting all elements by one place to the left and moving the first element to the last position in the array.

Example:
Input: 'a' = 5, 'arr' = [1, 2, 3, 4, 5]
Output: [2, 3, 4, 5, 1]
Explanation: We moved the 2nd element to the 1st position, and 3rd element to the 2nd position, and 
4th element to the 3rd position, and the 5th element to the 4th position, and move the 1st element to the 5th position.
'''

def rotateArray(arr,n):                 #Brute Force
    
    # Base Condition 
    if n == 0 or n == 1:
        return
    
    # Logic
    for i in range (n):
        arr[i] = arr[2]
    return arr

# Test Run 
print(rotateArray([1,2,3,4,5],5))
    
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
  #Brute Force
def rotateArray(arr,n):               
    
    # Base Condition 
    if n == 0 or n == 1:
        return
    
    # Logic
    temp = [0] * n 
    for i in range (1,n):
        temp[i-1] = arr[i]
        
    temp[n-1] = arr[0]
    return temp

# Test Run 
# print(rotateArray([1,2,3,4,5],5))
    
    
# Optimal Approach 
def leftRotate(arr,n):
    x = arr[0]
    for i in range (n-1):
        arr[i] = arr[i+1]
        
    arr[n-1] = x
    return arr
    
    
# Test Run 
# print(leftRotate([1,2,3,4,5],5))


# Leetcode 
def rotate(nums,k):
    n = len(nums)
    k %= n  #This will take number of rotations 
    def rrotate(l,r):
        while l < r :
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        
        
    rrotate(0,n-1)
    rrotate(0,k-1)
    rrotate(k,n-1)
    return nums
# Test Run 
# print(rotate([1,2,3,4,5,6,7],3))



# def Lrotate(arr,k):
#     n = len(arr)
#     k %= n
    
#     def rotations(l,r):
#         arr[l],arr[r] = arr[r],arr[l]
#         l += 1
#         r -= 1 
        
#     # rotations(0,k-1)
#     # rotations(k,n-k)
    
#     # OR this for left rotation
#     rotations(0, n - 1)
#     rotations(0, n - k - 1)
#     rotations(n - k, n - 1)
    
#     return arr

# # Test Run 
# print(Lrotate([7,5,2,11,2,43,1,1],2))
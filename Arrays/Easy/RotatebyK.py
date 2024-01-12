'''
Link > https://www.codingninjas.com/studio/problems/rotate-array_1230543?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM
Rotate array by K elements
Problem Statement: Given an array of integers, rotating array of elements by k elements either left or right.

Example:

Input: N = 7, array[] = {1,2,3,4,5,6,7} , k=2 , right
Output: 6 7 1 2 3 4 5
Explanation: array is rotated to right by 2 position .

'''

def rotateBy(arr,k):
    n = len(arr)
    
    for j in range (k):
        temp =  arr[0]
        for i in range (n-1):
            arr[i] = arr[i+1]
            
        arr[n-1] = temp
    return arr
# Test Run 
# print(rotateBy([7,5,2,11,2,43,1,1],2))

# Sample Output :
# 2 11 2 43 1 1 7 5
# Explanation :
# Rotate 1 steps to the left: 5 2 11 2 43 1 1 7
# Rotate 2 steps to the left: 2 11 2 43 1 1 7 5



# IF the direction is given 
def direction(arr,k,direction):
    n = len(arr)
    k %= n
    
    if direction == 'Left':
        for j in range (k):
            temp = arr[0]
            for i in range (n-1):
                arr[i] = arr[i+1]
                
            arr[n-1] = temp
            
    def rotateR(l,r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
            
            
            
    if direction == 'Right' :
    
        rotateR(0,n-1)
        rotateR(0,k-1)
        rotateR(k,n-1)
    return arr


# Test Case 
print(direction([7,5,2,11,2,43,1,1],2,'Right'))
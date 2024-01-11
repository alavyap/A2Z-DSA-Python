'''
Link > https://www.codingninjas.com/studio/problems/remove-duplicates-from-sorted-array_1102307?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse
Problem statement
You are given a sorted integer array 'arr' of size 'n'.
You need to remove the duplicates from the array such that each element appears only once.
Return the length of this new array.

Note:
Do not allocate extra space for another array. You need to do this by modifying the given input array in place with O(1) extra memory. 

For example:
'n' = 5, 'arr' = [1 2 2 2 3].
The new array will be [1 2 3].
So our answer is 3.
'''

def removeDupli(arr,n):     #This is the Brute Force  with usign SET > which only stores unique values 
    newSet = set()
    for i in range (n):
        newSet.add(arr[i])
    k = len(newSet)
    return k

# Optimized Way  
# LeetCode

def removeDuplicate(arr,n):
    if n == 0 or n == 1 :
        return
    
    k = 0
    for i in range (1,n):
            if arr[k] != arr[i]:
                k += 1
                arr[k] = arr[i]
                
    return k +1

# Test Run
print(removeDuplicate([1,2,2,2,3],5))
# print(removeDupli([1,2,2,2,3],5))


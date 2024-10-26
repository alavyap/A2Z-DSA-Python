'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/893046?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
LeetCode :>  https://leetcode.com/problems/next-permutation/description/
next_permutation : find next lexicographically greater permutation
Problem Statement: Given an array Arr[] of integers, rearrange the numbers of the given array into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange to the lowest possible order (i.e., sorted in ascending order).

Examples
Input format: Arr[] = {1,3,2}
Output: Arr[] = {2,1,3}
Explanation: All permutations of {1,2,3} are {{1,2,3} , {1,3,2}, {2,1,3} , {2,3,1} , {3,1,2} , {3,2,1}}. So, the next permutation just after {1,3,2} is {2,1,3}.
'''

# Optimal Code 
# Time Complexity  = O(n)
# Space Complexity  = O(1)

def lexi(arr):
    n = len(arr) - 2 
    while n >= 0 and arr[n] >= arr[n+1]:
        n -= 1
        
    # If no such element is found,reverse the entire array 
    if n == -1 :
        arr.reverse()
        return arr
    
    # Find the smallest element to the right of arr[i] and greater than  arr[i]
    j = len(arr) -1 
    while arr[j] <= arr[n] :
        j -= 1 
    
    # Swap arr[n] and arr[j] 
    arr[n], arr[j] = arr[j],arr[n]
    
    # Reverse the subarray to the right of arr[n]
    left, right = n+1 , len(arr) -1
    while left < right :
        arr[left],arr[right] = arr[right],arr[left]
        left += 1
        right -= 1
    # arr[n +1: ] = reversed(arr[n+1 :])  
    return arr


# Test Run 
print (lexi([2,3,1,4,5]))


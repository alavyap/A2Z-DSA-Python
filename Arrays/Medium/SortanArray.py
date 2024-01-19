'''
Link >> https://www.codingninjas.com/studio/problems/631055?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website
Link LeetCode >> https://leetcode.com/problems/sort-colors/
Problem Statement: Given an array consisting of only 0s, 1s, and 2s. 
Write a program to in-place sort the array without using inbuilt sort functions. 

( Expected: Single pass-O(N) and constant space)
Example:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


This is a variation of the popular Dutch National Flag Algorithm
'''

# Brute Force 
def sortArray(arr):
    n  = len(arr)
    for i in range (n):
        for j in range (i+1,n):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
                
    return arr

# Test Run 
# print(sortArray([2,0,2,1,1,0]))

# Optimal Approach 

def arraySort(nums):
    n = len(nums)
    low = 0
    mid = 0
    high = n-1
    # Time Cpmplexity >> O(N)
    # Space Complexity >> O(1)
    while mid <= high:
        if nums[mid] == 0 :
            nums[low],nums[mid] = nums[mid],nums[low]
            low += 1 
            mid += 1
            
        elif nums[mid] == 1:
            mid += 1
        # elif nums[mid] == 2 :
        else :
            nums[mid],nums[high] = nums[high],nums[mid]
            high -= 1
    return nums

# Test Run 
print(arraySort([2,0,2,1,1,0]))
    
    
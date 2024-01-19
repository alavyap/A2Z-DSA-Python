'''
Link :> https://www.codingninjas.com/studio/problems/majority-element_6783241?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse
LeetCode :> https://leetcode.com/problems/majority-element/
Problem Statement: Given an array of N integers, write a program to return an element that occurs more than N/2 times in the given array. 
You may consider that such an element always exists in the array.

Example
Input Format: N = 3, nums[] = {3,2,3}
Result: 3
Explanation: When we just count the occurrences of each number and compare with half of the size of the array, you will get 3 for the above solution. 

THis Problem uses "Moore's Voting Algorithm"
'''
# Brute Force 
from os import major


def majority(nums):
    n = len(nums)
    mid = n//2
    store = {}
    for i in range (n):
        if nums[i] in store :
            store[nums[i]] += 1
        else:
            store[nums[i]] = 1
    
    for key,value in store.items():
        if value > mid:
            return key       
        
        
# Test Run 
# print (majority([2,2,1,1,1,2,2]))

# Optimal Approach
   

   
'''
Moore's Voting Algorithm


def majorityElement(nums):
    majority = None 
    count = 0 
    
    for i in range (n):
        if count == 0 :
            count = 1
            majority = nums[i]
        elif majority == nums[i] :
            count += 1
        else:
            count -= 1
            
    count1 = 0
    for i in range (n):
        if nums[i] == majority:
            count1 += 1
            
    if count1 > mid :
        return majority 
    return -1
    
'''
# Time Cpmplexity >> O(N)
# Space Complexity >> O(1)
def majorityElement(nums):
    count = 0
    majority = None 
    for ele in nums :
        if count == 0 :
            majority = ele 
        
        if ele == majority :
            count += 1
        else :
            count -= 1
    return majority
# Test Run
print (majorityElement([2,2,1,1,1,2,2]))
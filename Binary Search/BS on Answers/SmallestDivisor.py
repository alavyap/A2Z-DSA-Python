'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/smallest-divisor-with-the-given-limit_1755882
LeetCode :> https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/

Problem Statement: You are given an array of integers ‘arr’ and an integer i.e. a threshold value ‘limit’. 
Your task is to find the smallest positive integer divisor, such that upon dividing all the elements of the given array by it, 
the sum of the division’s result is less than or equal to the given threshold value.

Example :
Input Format: N = 5, arr[] = {1,2,3,4,5}, limit = 8
Result: 3
Explanation: We can get a sum of 15(1 + 2 + 3 + 4 + 5) if we choose 1 as a divisor. 
The sum is 9(1 + 1 + 2 + 2 + 3)  if we choose 2 as a divisor. Upon dividing all the elements of the array by 3, we get 1,1,1,2,2 respectively.
Now, their sum is equal to 7 <= 8 i.e. the threshold value. So, 3 is the minimum possible answer.
'''

# Brute Force 
import math 
def brute (arr,limit):
    n = len(arr)
    maxi = max(arr)
    for i in range (1,maxi):
        if summation(arr,i) <= limit :
            return i 
    return -1

# Helper Function 
def summation(arr,div):
    n = len(arr)
    total = 0
    for i in range (n):
        total += math.ceil(arr[i]/div)
    return total

# Test Run 
# print(brute([1,2,3,4,5],8))

# Optimal Approach
def optimal (arr,limit):
    low = 1 
    high = max(arr)
    
    while (low <= high):
        mid = (low + high) // 2 
        
        if divisor(arr,mid) <= limit:
            high = mid -1 
        
        else:
            low = mid +1 
    return low        
# def helper 
def divisor(arr,divi):
    n = len(arr)
    totalS = 0 
    for i in range (n):
        totalS += math.ceil(arr[i]/divi)
    return totalS

# Test Run 
print(optimal([1,2,3,4,5],8))
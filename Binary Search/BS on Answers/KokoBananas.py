'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/minimum-rate-to-eat-bananas_7449064
Problem Statement: A monkey is given n piles of bananas, whereas the ith pile has a[i] bananas.
An integer h is also given, which denotes the time (in hours) for all the bananas to be eaten.
Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas. 
If the pile contains less than k bananas, then the monkey consumes all the bananas and won't eat any more bananas in that hour.
Find the minimum number of bananas k to eat per hour so that the monkey can eat all the bananas within h hours.

Example :
Input Format: N = 4, a[] = {7, 15, 6, 3}, h = 8
Result: 5
Explanation: If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. So, he will take 8 hours to complete all the piles.  

'''
# Brute Force 
from math import ceil
import math


def brute (arr,h):
   
   maxi = highEle(arr)
   for i in range (1,maxi+1):
       reqTime = calculateHours(arr,i)
       if reqTime <= h :
           return i 
       
       
# Function to calculate hours to complete eating 
def calculateHours(arr,mini):
    totalH = 0 
    n = len(arr)
    for i in range (n):
        totalH += ceil(arr[i]/ mini)
    return totalH
    
   
# Function for getting max element 
def highEle(arr):
    n = len(arr) 
    maxi = float('-inf')
    for i in range (n):
        maxi = max(maxi,arr[i])
    return maxi 

# Test Run 
# print(brute ([7,15,6,3],8))


# Optimal Approach 
def optimal (arr,h):
    n = len(arr)
    low = 1 
    high = maxi(arr)
    
    while (low <= high):
        mid = (low + high) //2 
        reqTime = totalTime(arr,mid) 
        
        if reqTime <= h :
            high = mid - 1 
        else :
            low = mid + 1 
    
    return low 
    
    
# Finding the max 
def maxi(arr):
    n = len(arr)
    maxo = float('-inf')
    for i in range (n):
        maxo = max(maxo,arr[i])
        
    return maxo 


# Finding the Total time 
def totalTime(arr,hour):
    totalH = 0 
    n = len(arr)
    for i in range (n):
        totalH += math.ceil(arr[i]/hour)
    return totalH

# Test Run 
print(optimal ([7,15,6,3],8))

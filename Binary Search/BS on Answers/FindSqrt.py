'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/square-root-integral_893351?leftPanelTab=0%3Futm_source%3Dstriver

Problem Statement: You are given a positive integer n. Your task is to find and return its square root. 
If 'n' is not a perfect square, then return the floor value of 'sqrt(n)'.

Note: The question explicitly states that if the given number, n, is not a perfect square, our objective is to find the maximum number, x, 
such that x squared is less than or equal to n (x*x <= n). In other words, we need to determine the floor value of the square root of n.

Example :
Input Format: n = 28
Result: 5
Explanation: Square root of 28 is approximately 5.292. So, the floor value will be 5.
'''
# Brute Force
import math 
def brute(n):
    # Edge Case 
    if n == 0 or n == 1 :
        return n
     
    srt = n ** 0.5
    ans = math.floor(srt)
    return ans

# Test Run 
# print(brute(6))

# Optimal Approach 
def optimal (n):
   
    low = 1 
    high = n 
    while (low <= high):
        mid = (low + high) //2 
        
        ans = mid * mid 
        
        if ans <= n :
            low = mid +1 
        else :
            high = mid - 1 
    return high
        
        

# Test Run 
print(optimal(6))
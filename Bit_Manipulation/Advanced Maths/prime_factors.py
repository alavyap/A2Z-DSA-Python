'''
GFG :> https://www.geeksforgeeks.org/problems/prime-factors5052/1

Given a number N. Find its unique prime factors in increasing order.

Example 1:

Input: N = 100
Output: 2 5
Explanation: 2 and 5 are the unique prime
factors of 100.
Example 2:

Input: N = 35
Output: 5 7
Explanation: 5 and 7 are the unique prime
factors of 35.
 

Your Task:
You don't need to read or print anything. Your task is to complete the function AllPrimeFactors() which takes N as input parameter and returns a list of all unique prime factors of N in increasing order.

 

Expected Time Complexity: O(N)
Expected Space Complexity: O(N)
 

Constraints:
1 <= N  <= 106
'''

# Brute Force 

def prime(n):
    factors = set()
    divisor = 2 
    
    while divisor * divisor <= n :
        if n % divisor == 0 : 
            factors.add(divisor)
            n //= divisor
            
        else:
            divisor += 1 
    if n >1 :
        factors.add(n)
            
    return factors

# Test Run 
print(prime(100))
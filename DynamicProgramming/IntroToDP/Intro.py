'''
Problem Statement:  Introduction To Dynamic Programming

In this article, we will be going to understand the concept of dynamic programming.

Dynamic Programming can be described as storing answers to various sub-problems to be used later whenever required to solve the main problem.

The two common dynamic programming approaches are:

Memoization: Known as the “top-down” dynamic programming, usually the problem is solved in the direction of the main problem to the base cases.
Tabulation: Known as the “bottom-up '' dynamic programming, usually the problem is solved in the direction of solving the base cases to the main problem


We will be using the example of Fibonacci numbers here. The following series is called the Fibonacci series:

0,1,1,2,3,5,8,13,21,...

We need to find the nth Fibonacci number, where n is based on a 0-based index.

Every ith number of the series is equal to the sum of (i-1)th and (i-2)th number where the first and second number is given as 0 and 1 respectively.

'''

# Memoization Way 
def func(n,dp):
    
    if n <= 1 : 
        return n     
    if dp[n] != -1 :
        return dp[n] 
    dp[n] = func(n-1,dp) + func(n-1,dp)
    return dp[n] 

if __name__ == "__main__":
    n = 5
    dp = [-1] * (n+1)
    print(func(n, dp))
    
    
# Tabulation Way 
def main ():
    
    n = 5 
    dp = [-1] * (n+1)
    dp[0] = 0 
    dp[1] = 1 
    
    for i in range (2,n+1): 
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])
    
    
# Space Optimization 
def spaceOp():
    n = 5 
    prev2 = 0 
    prev = 1 
    
    for i in range (2,n+1): 
        curI = prev2 + prev 
        prev2 = prev 
        prev = curI
    print(prev) 
        
'''
Link :> https://leetcode.com/problems/climbing-stairs/description/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:
1 <= n <= 45
'''

# Memoization 

def stairs(n):
    dp = [-1]  * (n+1)
    return helper(n,dp)

def helper(n,dp):
    
    if n <= 1 :
        return 1
    if dp[n] != -1: 
        return dp[n] 
    dp[n] = helper(n-1,dp) + helper(n-2,dp) 
    return dp[n]
    
    
# Tabulation 

def stairsClimb(n):
    dp= [-1] * (n+1)
    dp[0] = 1 
    dp[1] = 1
    
    for i in range (2,n+1): 
        dp[i] = dp[i-1] + dp[i-2]
    return (dp[n])



# Space Optimization 

def fastClimb(n):
    prev2 = 1 
    prev = 1 
    for i in range (2,n+1):
        curr = prev2 + prev 
        prev2 = prev 
        prev = curr 
    return (prev)
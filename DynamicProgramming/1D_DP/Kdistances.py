'''
Problem Statement:
This is a follow-up question to “Frog Jump” discussed in the previous article. In the previous question, the frog was allowed to jump either one or two steps at a time. In this question, the frog is allowed to jump up to ‘K’ steps at a time. If K=4, the frog can jump 1,2,3, or 4 steps at every index.
'''

# Memoization 
def helper(index,height,dp,k):
    if index == 0 : 
        return 0 
    
    if dp[index] != -1:
        return dp[index]
    
    
    mmSteps = float("inf")
    
    for j in range (1, k+1):
        if index - j >= 0 : 
            jump = helper(index-j,height,dp,k) + abs(height[index] - height[index - j ])
            mmSteps = min(jump,mmSteps)
    
    dp[index] = mmSteps
    return dp[index]

# finding the minimum cost to reach the end of array 

def solve(n,height,k):
    dp=[-1] *n 
    return  helper(n-1,height,dp,k)

def main (height,k):
    n = len(height)
    return (solve(n,height,k))
    
    
    
    
# Tabulation 
def helper(n,height,dp,k):
    dp[0] = 0 
    
    for i in range (1, n):
        mmSteps = float("inf")
        for j in range (1,k+1): 
            if i-j >= 0 : 
                jump = dp[i-j] + abs(height[i] - height[i-j])
                mmSteps = min(jump,mmSteps)
        dp[i] = mmSteps
    return dp[n-1]

def solve(n,height,k): 
    dp = (float("-inf") ) * n 
    return helper(n,height,dp,k)
    
def main(height,k):
    n = len(height)
    result = solve(n,height,k)
    return result
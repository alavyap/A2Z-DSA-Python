'''
Link :> https://leetcode.com/problems/distinct-subsequences/description/

Given two strings s and t, return the number of distinct subsequences of s which equals t.
The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
'''

# Memoization 
prime = int(1e9 +7)
def numDistinct(s,t):
    n = len(s)
    m = len(t)
    
    dp = [[-1 for _ in range (m)] for _ in range (n)]
    return helper(s,t,n-1,m-1,dp)

def helper(s,t,ind1,ind2,dp):
    
    if ind2 < 0 : 
        return 1 
    if ind1 < 0 :
        return 0 
    
    if dp[ind1][ind2] != -1: 
        return dp[ind1][ind2]
    
    if s[ind1] == t[ind2]:
        leaveOne = helper(s,t,ind1 -1,ind2 -1,dp)
        stay = helper(s,t,ind1-1,ind2,dp)
        
        dp[ind1][ind2] = (leaveOne + stay) % prime
        return dp[ind1][ind2]
    else :
        dp[ind1][ind2] = helper(s,t,ind1-1,ind2,dp)
        return dp[ind1][ind2]
    
    
# Tabulation 
def distinctSub(s,t):
    n = len(s)
    m = len(t)
    
    dp = [[0 for _ in range (m +1)] for _ in range (n +1)]
    
    for i in range (n +1): 
        dp[i][0] = 1 
    
    for j in range (1,m +1): 
        dp[0][j] = 0
        
    for i in range (1,n +1):
        for j in range (1,m+1): 
            dp[i][j] = (dp[i-1][j-1] + dp[i -1][j]) % prime if s[i -1] == t[j -1] else dp[i-1][j]
    return dp[n][m]

# Space Optimization
def subsequent(s,t):
    n = len(s)
    m = len(t)
    
    prev = [0 for _ in range (m+1)]
    prev[0] = 1 
    
    for i in range (1,n+1): 
        for j in range (m,0, -1):
            if s[i-1] == t[j-1]: 
                prev[j] = (prev[j-1]+ prev[j]) % prime
            else: 
                prev[j] = prev[j]
                
    return prev[m]
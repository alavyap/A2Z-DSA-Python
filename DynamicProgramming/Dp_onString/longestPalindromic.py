'''
Link :> 

Given a string s, find the longest palindromic subsequence's length in s.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
 

Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
'''

# Tabulation 

def longestPalindrome(s): 
    t = s
    s = s[::-1]   
    n = len(t)
    m = len(s)
        
    dp = [[-1] * (m +1) for _ in range (n+1)]
        
    for i in range (n+1): 
        dp[i][0] = 0 
    for i in range (m+1): 
        dp[0][i] = 0 
            
    for ind1 in range (1,n+1):
        for ind2 in range (1,m +1): 
            if t[ind1 -1] == s[ind2 -1]: 
                dp[ind1][ind2] = 1 + dp[ind1 -1][ind2 -1]
            else: 
                dp[ind1][ind2] = max(dp[ind1 -1][ind2],dp[ind1][ind2 -1])    
    return dp[n][m]

# Space Optimization 

def lps(s): 
    n = len(s)
    curr = [0]*n
    prev = [0]*n
    for i in range(n-1,-1,-1):
        curr[i] = 1
        for j in range(i+1,n):
            if s[i] == s[j]:
                curr[j] = prev[j-1]+2
            else:
                curr[j] = max(prev[j],curr[j-1])
        prev = curr[:]
    return curr[n-1]
'''
Link :> https://leetcode.com/problems/longest-common-subsequence/description/

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
 

Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.

'''

# Memoization 
def longestCommonS(text1,text2): 
    n = len(text1)
    m = len(text2)
    
    dp = [[-1 for _ in range (m)]for _ in range (n)]
    return helper(text1,text2,n-1,m-1,dp)

def helper(t1,t2,ind1,ind2,dp): 
    if ind1 <0 or ind2 <0 : 
        return 0 
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
    
    
    if t1[ind1] == t2[ind2]:
        dp[ind1][ind2] = 1 + helper(t1,t2,ind1 - 1,ind2 -1,dp)
    else:
        dp[ind1][ind2] = max(helper(t1,t2,ind1,ind2-1,dp), helper(t1,t2,ind1 -1,ind2,dp))

    return dp[ind1,ind2]


# Tabulation 

def longestSubsequence(text1,text2):
    
    n= len(text1)
    m = len(text2)
    
    dp = [[-1 for _ in range (m+1)] for  _ in range (n +1)]
    
    for i in range (n +1):
        dp[i][0] = 0 
    for j in range (m +1): 
        dp[0][j] = 0 
            
    for ind1 in range ( 1, n +1): 
        for ind2 in range (1,m +1):
            if text1[ind1 -1] == text2[ind2 -1]: 
                dp[ind1][ind2] = 1 + dp[ind1 -1 ][ind2 -1 ]
            else: 
                dp[ind1][ind2] = max(dp[ind1 -1][ind2], dp[ind1][ind2 -1])
                
    return dp[n][m] 


# Space Optimization 

def lcs(text1,text2): 
    
    n = len(text1)
    m = len(text2)
    
    prev = [0] * (m+1)
    curr = [0] * (m +1)
    
    for ind1 in range (1, n + 1): 
        for ind2 in range (1,m +1): 
            if text1[ind1 -1] == text2[ind2 -1]: 
                curr[ind2] = 1 + prev[ind2 - 1]
            else: 
                curr[ind2] = max(prev[ind2], curr[ind2 -1])
        prev = curr[:]
    return prev[m]
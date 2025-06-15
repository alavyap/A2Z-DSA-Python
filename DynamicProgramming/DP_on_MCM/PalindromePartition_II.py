'''
Link :> https://leetcode.com/problems/palindrome-partitioning-ii/description/

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s. 

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1
 
 
Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.
'''

# Memoization << This will give TLE 

def minCut(s):
    n = len(s)
    dp = [-1] * n 
    
    is_palindrome = [[False] * n for _ in range (n)]
    
    for i in range (n): 
        is_palindrome[i][i] = True 
        
    for i in range (n-1): 
        if s[i] == s[i+1]:
            is_palindrome[i][i+1] = True 
            
            
    for length in range (3,n+1): 
        for i in range (n - length +1):
            j = i + length -1 
            if s[i] == s[j] and is_palindrome[i+1][j-1]: 
                is_palindrome = True 

    return helper(0,n,s,dp, is_palindrome) -1


def helper(i,n,s,dp, is_palindrome): 
    if i == n :
        return 0 
    
    if dp[i] != -1 :
        return dp[i] 
    
    minCost = float("inf")
    
    for j in range (i,n):
        if is_palindrome[i][j]:
            cost = 1 + helper(j +1,n,s,dp,is_palindrome)
            minCost = min(minCost,cost)
    dp[i] = minCost 
    return dp[i] 

# Tabulation 

def Cutmin(s):

    n = len(s)
    is_palindrome = [[False] * n for _ in range (n)]
   
    for i in range (n):
       is_palindrome[i][i] = True
    
    for i in range (n-1):
        if s[i] == s[i+1]: 
            is_palindrome[i][i+1] = True
            
    for length in range (3,n+1): 
        for i in range (n - length +1):
            j = i +length - 1
            if s[i] == s[j] and is_palindrome[i +1][j-1]: 
                is_palindrome[i][j] = True
                
    dp = [float("inf")] * (n +1)
    dp[n] = 0 
    
    for i in range (n-1,-1,-1): 
        for j in range (i,n):
            if is_palindrome[i][j]: 
                dp[i] = min(dp[i],1 + dp[j+1])
                
    return dp[0] -1
        
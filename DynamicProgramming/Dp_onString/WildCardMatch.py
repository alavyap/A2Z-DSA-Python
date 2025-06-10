'''
Link :> https://leetcode.com/problems/wildcard-matching/description/

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Constraints:

0 <= s.length, p.length <= 2000
s contains only lowercase English letters.
p contains only lowercase English letters, '?' or '*'.
'''

# Memoization
def wildcard(s,p): 
    n = len(s)
    m = len(p)
    
    dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
    return helper(p, s, m - 1, n - 1, dp)

def helper(pat, s, i, j, dp):
    if i < 0 and j < 0:
        return True
    if i < 0 and j >= 0:
        return False
    if j < 0 and i >= 0:
        return checkStars(pat, i)

    if dp[i][j] != -1:
        return dp[i][j]

    if pat[i] == s[j] or pat[i] == '?':
        dp[i][j] = helper(pat, s, i - 1, j - 1, dp)
    elif pat[i] == '*':
        dp[i][j] = helper(pat, s, i - 1, j, dp) or helper(pat, s, i, j - 1, dp)
    else:
        dp[i][j] = False
    return dp[i][j]

def checkStars(p, i):
    for j in range(i + 1):
        if p[j] != '*':
            return False
    return True



# Tabulation 
def wildcards(s,p): 
    n = len(s)
    m = len(p)
    
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = True
    
    for j in range(1, m + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
            
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    return dp[n][m]
        

# Space Optimization
def matchCards(s,p):
    n = len(s)
    m = len(p)
    
    prev = [False] * (m + 1)
    curr = [False] * (m + 1)
    
    prev[0] = True

    # Handle pattern only with '*' when string is empty
    for j in range(1, m + 1):
        if p[j - 1] == '*':
            prev[j] = prev[j - 1]
        else:
            break

    for i in range(1, n + 1):
        curr[0] = False  # when pattern is empty, no match
        for j in range(1, m + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                curr[j] = prev[j - 1]
            elif p[j - 1] == '*':
                curr[j] = prev[j] or curr[j - 1]
            else:
                curr[j] = False
        prev, curr = curr, [False] * (m + 1)
    
    return prev[m]
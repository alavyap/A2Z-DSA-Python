'''
Link :> https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/ 

Given a string s. In one step you can insert any character at any index of the string.
Return the minimum number of steps to make s palindrome.
A Palindrome String is one that reads the same backward as well as forward. 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.

Example 2:
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Example 3:
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.
'''

# Tabulation 
def minInsertion(s):
    t = s[::-1] 
    n = len(s)
    m = len(t)
    
    dp = [[-1 for _ in range (m+1)] for _ in range (n +1)]
    
    for i in range (n+1):
        dp[i][0] = 0 
    for j in range (m +1): 
        dp[0][j] = 0 
        
    for ind1 in range (1, n+1): 
        for ind2 in range (1,m +1): 
            if s[ind1 -1 ] == t[ind2 - 1]: 
                dp[ind1][ind2] = 1 + dp[ind1 -1][ind2 -1]
            else: 
                dp[ind1][ind2]  = max(dp[ind1 -1][ind2], dp[ind1][ind2 -1])
    return n - dp[n][m] 



# Space Optimization 

def insertMin(s):
    t = s 
    s = s[::-1]
    
    n = len(s)
    m = len(t)
    
    prev = [0] * (m +1)
    curr = [0] * (m + 1)
    
    for ind1 in range (1,n +1): 
        for ind2 in range (1,m +1): 
            if s[ind1 -1] == t[ind2 -1]: 
                curr[ind2] = 1 + prev[ind2 -1]
            else: 
                curr[ind2] = max(prev[ind2], curr[ind2 -1])
        prev = curr[:]        
    return n - prev[m]
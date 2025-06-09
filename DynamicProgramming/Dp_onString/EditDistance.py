'''
Link :> https://leetcode.com/problems/edit-distance/description/

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 
Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
'''

# Memoization 
def min(word1,word2): 
    
    n = len(word1)
    m = len(word2)    
    dp = [[ -1 for _ in range (m)] for _ in range (n)]
    return helper(word1,word2,n-1,m-1,dp)

def helper(str1,str2,i,j,dp): 
    
    if i < 0 :return j + 1
    if j < 0 : return i +1
    
    if dp[i][j] != -1:
        return dp[i][j] 
    if str1[i] == str2[j]: 
        dp[i][j] = helper(str1,str2,i-1,j-1,dp)
    else:
        dp[i][j] = 1 + min(
            helper(str1,str2,i-1,j-1,dp),
            min(helper(str1,str2,i-1,j,dp), helper(str1,str2,i,j-1,dp))
        )        
    return dp[i][j]


# Tabulation 
def minDistance(word1,word2): 
    
    n = len(word1)
    m = len(word2)
    
    dp = [[0 for _ in range (m+1)] for _ in range (n +1)]
    
    for i in range (n +1):
        dp[i][0] = i 
    for j in range (m+1):
        dp[0][j] = j 
        
    for i in range (1,n+1): 
        for j in range (1, m +1): 
            
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else: 
                dp[i][j] = 1 + min(dp[i-1][j -1], min(dp[i-1][j],dp[i][j-1]))
                
    return dp[n][m]

# Space Optimization
def minCount(word1,word2): 
    
    n = len(word1)
    m = len(word2)
    
    prev = [j for j in range (m +1)]
    curr = [0 for _ in range (m +1)]
    
    for i in range (1, n+1): 
        curr[0] = i 
        
        for j in range (1, m+1): 
            if word1[i-1] == word2[j-1]: 
                curr[j] = prev[j-1]
            else: 
                curr[j] = 1 + min(prev[j-1], min(prev[j],curr[j-1]))
        prev, curr = curr,prev 
    return prev[m]    
            
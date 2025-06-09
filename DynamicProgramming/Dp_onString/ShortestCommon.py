'''
Link :> https://leetcode.com/problems/shortest-common-supersequence/description/

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s. 

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.
'''

def shortestSupersequence(str1,str2): 
    
    n = len(str1)
    m = len(str2)
    
    dp = [[0 for _ in range (m +1)] for _ in range (n +1)]
    
    for i in range (n +1): 
        dp[i][0] = 0 
    for j in range (m +1): 
        dp[0][j] = 0 
        
    for ind1 in range (1, n +1): 
        for ind2 in range (1,m +1): 
            if str1[ind1 -1] == str2[ind2 -1]: 
                dp[ind1][ind2] = 1 + dp[ind1 -1][ind2 -1]
            else: 
                dp[ind1][ind2] = 0 + max(dp[ind1 -1][ind2],dp[ind1][ind2 -1])
    
    lenght = dp[n][m] 
    i = n 
    j = m 
    
    index = lenght - 1
    ans = ""
    
    while i > 0 and j > 0 : 
        if str1[i-1] == str2[j -1]:
            ans += str1[i -1]
            index -= 1
            i -= 1 
            j -= 1 
        elif dp[i -1][j] > dp[i][j-1]: 
            ans += str1[i -1]
            i -= 1 
        else: 
            ans += str2[j -1]
            j -= 1 
            
    while i > 0 : 
        ans += str1[i -1]
        i -= 1 
    while j > 0 : 
        ans += str2[j -1]
        j -= 1 
    
    ans = ans[::-1]
    return ans 



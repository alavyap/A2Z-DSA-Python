'''
GFG :> https://www.geeksforgeeks.org/problems/better-string/1

Given a pair of strings of equal lengths, Geek wants to find the better string. The better string is the string having more number of distinct subsequences.
If both the strings have equal count of distinct subsequence then return str1.

Example 1:

Input:
str1 = "gfg", str2 = "ggg"
Output: "gfg"
Explanation: "gfg" have 6 distinct subsequences whereas "ggg" have 3 distinct subsequences. 

Your Task:
You don't need to read input or print anything. Your task is to complete the function betterString() which takes str1 and str2 as input parameters and returns the better string.
Expected Time Complexity: O( N ), where N is the length of both provided strings.
Expected Auxiliary Space: O( N )

'''


# Time :. O(N) and Space :. O(N)
def if_better (str1,str2):
    
    c1 = count_subsequence(str1)
    c2 = count_subsequence(str2)
    
    if c1 > c2 :
        return str1 
    elif c1 < c2 :
        return str2
    else :
        return str1 
    
    
def count_subsequence (str):
    n = len(str)
    MOD = 10 ** 9 + 7
    
    dp = [0] * (n +1)
    dp[0] = 1 
    last_occurences = {}
    
    for [i] in range (1, n+1):
        dp[i] = (2 * dp[i-1]) % MOD
        
        if str[i-1] in last_occurences :
            dp[i] = (dp[i] - dp[last_occurences[str[i-1]] - 1 ]) % MOD 
        
        last_occurences[str[i-1]] = i 
        
    return  dp[n]    
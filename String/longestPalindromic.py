'''
LeetCode :> https://leetcode.com/problems/longest-palindromic-substring/description/
Given a string s, return the longest 
palindromic substring in s.

Example :
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

'''
# Brute Force 
def palindromic(s):
    res = ""
    resLen= 0 
    
    for i in range (len(s)):
        
        # Odd Length
        l,r = i,i 
        while l >= 0 and r < len(s) and s[l] == s[r] :
            if (r - l +1) > resLen:
                res = s[l:r+1]
                resLen = r - l + 1
            l -= 1 
            r += 1 
        # Even Length 
        l,r= i ,i+1
        
        while l >= 0 and r <len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen :
                res = s[l:r+1]
                resLen = r- l +1
                
            l -= 1 
            r += 1 
            
    return res

# Time Complexity will be O(N^3)

# Test Run
print(palindromic("babad"))
    
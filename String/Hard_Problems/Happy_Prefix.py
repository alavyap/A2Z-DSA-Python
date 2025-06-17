'''
Link :> https://leetcode.com/problems/longest-happy-prefix/description/

A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists. 

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
 

Constraints:

1 <= s.length <= 105
s contains only lowercase English letters.

'''

def happyPrefix(s): 
    n = len(s)
    lps = [0] * n 
    length = 0 
    
    for i in range (1,n):
        while length > 0 and s[i] != s[length]: 
            length = lps[length -1]
        if s[i] == s[length]: 
            length += 1 
            lps[i] = length 
    return s[:lps[-1]]
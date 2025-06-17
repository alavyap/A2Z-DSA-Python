'''
Link :> https://leetcode.com/problems/shortest-palindrome/description/


You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation. 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:
Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
'''

def shortestPalindrome(s): 
    count = kmp(s[::-1],s)
    return s[count:][::-1] + s 

def kmp(txt,patt):
    new_string = patt + "#" + txt
    pi  = [0] * len(new_string)
    i = 1 
    k = 0 
    
    while i < len(new_string): 
        if new_string[i] == new_string[k]:
            k += 1 
            pi[i] = k 
            i += 1 
        else: 
            if k > 0 :
                k  = pi[k-1]
            else: 
                pi[i] = 0 
                i += 1 
    return pi[-1]
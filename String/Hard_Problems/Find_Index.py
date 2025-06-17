'''

Link :> https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''



# Z -Function 
def str(haystack,needle):
    if not needle: 
        return 0 
    
    concat = needle + "#" + haystack
    z = computeZ(concat)
    needle_len = len(needle)
    
    for i in range (len(needle) + 1, len(concat)): 
        if z[i] == needle_len: 
            return i - needle_len -1 
    return -1 

def computeZ(s):
    n = len(s)
    z = [0] * n 
    l = r= 0 
    
    for i in range (1,n):
        if i <= r: 
            z[i] = min(r-i + 1, z[i-l] )
        while i + z[i] < n and s[z[i]] == s[i +z[i]]: 
            z[i] += 1 
        if i + z[i] - 1 > r: 
            l,r = i,i + z[i] -1 
    return z 






























#  KMP Algo /LPS  

def strStr(haystack,needle): 
    
    if not needle: 
        return 0 
    
    lps = build_lps(needle)
    i = j = 0 
    
    while i < len(haystack): 
        if haystack[i] == needle[j]:
            i += 1 
            j += 1 
            if j == len(needle):
                return i - j
        elif j > 0 : 
            j = lps[j-1]
        else: 
            i += 1 
    return -1

def build_lps(pattern): 
    lps = [0] * len(pattern)
    length = 0 
    i = 1 
    
    while i < len(pattern): 
        if pattern[i] == pattern[length]: 
            length += 1
            lps[i] = length 
            i += 1 
        elif length > 0 : 
            length = lps[length -1 ]
        else: 
            lps[i] = 0 
            i += 1 
    return lps

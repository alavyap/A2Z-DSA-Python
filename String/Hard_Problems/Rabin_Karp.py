'''
Link :> https://leetcode.com/problems/repeated-string-match/description/


Given two strings a and b, return the minimum number of times you should repeat string a so that string b is a substring of it. If it is impossible for b​​​​​​ to be a substring of a after repeating it, return -1.
Notice: string "abc" repeated 0 times is "", repeated 1 time is "abc" and repeated 2 times is "abcabc".

 

Example 1:

Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.
Example 2:

Input: a = "a", b = "aa"
Output: 2
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist of lowercase English letters.
'''

BASE = 10 ** 6

def repeated(a,b):
    
    if a == b :
        return 1 
    
    count = 1 
    source = a 
    
    while len(source) < len(b):
        count += 1 
        source += a 
        
    if source == b: 
        return count 
    
    if rabin_karp(source,b) != -1 :
        return count 
    if rabin_karp(source,b) != -1: 
        return count 
    if rabin_karp(source + a,b) != -1: 
        return count + 1 
    
    return -1 


def rabin_karp(source,target): 
    if not source or not target:
        if not source or not target: 
            return -1 
        
    m = len(target)
    power = 1
    for _ in range (m): 
        power = (power * 31) % BASE 
    
    
    target_hash = 0 
    for ch in target: 
        target_hash = (target_hash * 31 + ord(ch)) % BASE
    
    hash_code = 0 
    for i in range (len(source)): 
        hash_code = (hash_code * 31 + ord(source[i])) % BASE 
        if i < m -1 : 
            continue 
        if i >= m : 
            hash_code = (hash_code - ord(source[i-m]) * power) % BASE
        
        if hash_code < 0: 
            hash_code += BASE
        if hash_code == target_hash:
            if source[i-m + 1: i +1] == target: 
                return i - m +1 
    return -1


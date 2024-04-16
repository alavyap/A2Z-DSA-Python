'''
Coding Ninja :> https://www.naukri.com/code360/problems/anagram-pairs_626517
LeetCode :> https://leetcode.com/problems/valid-anagram/description/
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example :
Input: s = "anagram", t = "nagaram"
Output: true
'''

# Brute Force 
def validAnagram(s,t):
    n = len(s)
    m = len(t)
    
    if n != m :
        return False 
    
    s1 =''.join(sorted(s))
    s2 = ''.join(sorted(t))
    
    
    for charS ,charT in zip(s1,s2):
        if charS != charT :
            return False
        
    return True
    

# Test Run 
s = "anagram"
t = "nagaram"

print(validAnagram(s,t))



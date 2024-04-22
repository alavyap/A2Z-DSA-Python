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
# s = "anagram"
# t = "nagaram"

# print(validAnagram(s,t))


# Better  Approach
# Time Complexity and Space Complexity = (s +t)

def anagramValid(s,t):
    if len(s) != len(t):
        return False
    
    countS, countT = {},{}
    
    
    for ele in range (len(s)):
        countS[s[ele]] = 1 + countS.get(s[ele],0)
        countT[t[ele]] = 1 + countT.get(t[ele],0)
        
    for charc in countS :
        if countS[charc] != countT.get(charc,0):
            return False 
    return True


# Test Run    
# s = "anagram"
# t = "nagaram"

# print(anagramValid(s,t))


# Optimal Approach 
# Time Complexity = O(n) & Space Complexity = O(1)

def checkAnagram(s,t):
    numberOfLetters = 26 
    s = s.lower()
    t = t.lower() 
    
    
    if len(s) != len(t):
        return False
    
    count = [0 for ele in range (numberOfLetters)]
    
    for ele in range (len(s)) :
        count [ord(s[ele]) - ord('a')] += 1 
        
    for ele in range (len(t)):
        count [ord(t[ele]) - ord('a')] -= 1 
        
    
    for ele in range (numberOfLetters):
        if count[ele] != 0  :
            return False 
        
    return True    
    

# Test Run    
s = "anagram"
t = "nagaram"

print(checkAnagram(s,t))
    
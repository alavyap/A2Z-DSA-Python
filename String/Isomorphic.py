'''
Coding Ninja :> https://www.naukri.com/code360/problems/isomorphic-strings-_1117636
LeetCode :> https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example :
Input: s = "egg", t = "add"
Output: true
'''

# Brute Force 

def isomorphic(str1,str2):
    hash1 = {}
    hash2 = {}
    n = len(str1)
    m = len(str2)
   
    if n != m:
        return False
    
    for char in str1 :
        if char in hash1 :
            hash1[char] += 1 
        else :
            hash1[char] = 1
    
    for chara in str2 :
        if chara in hash2 :
            hash2[chara] += 1 
        else:
            hash2[chara] = 1
            
    key1 = len(hash1)
    key2 = len(hash2)

    # count1 = len(hash1)  # Calculate the number of keys in hash1
    
    if key1 == key2:
        return True
    else: 
        return False 


    
# Test Run 
s= "egg"
t= "add"
# print(isomorphic(s,t))

# Optimal Approach
def isomorphicWords(s,t):
    mapST = {}
    for indx in range (len(s)):
        char1,char2 = s[indx],t[indx]
        if char1 not in mapST :
            if char2  in mapST.values() :
                return False 
            mapST[char1] = char2
        elif mapST[char1] != char2 :
            return False 
        
    return True

# Test Run 
print(isomorphicWords(s,t))


# NeetCode 
def isIso(s,t):
    mapST,mapTS = {},{}
    
    for c1,c2 in zip(s,t):
        if ((c1 in mapST and mapST[c1] != c2) or 
            (c2 in mapTS and mapTS[c2] != c1)):
            return False 
        mapST[c1] = c2
        mapTS[c2] = c1
    return True
'''

LeetCode :>  https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?



'''
# Time and Space Complexity : O(N+ M)
def twoWin(s,t):
    if not s or not t :
       return ""
    
    
    #    To count the frequnecy in t 
    mpp_t= {}
    for char in t :
        mpp_t[char] = mpp_t.get(char, 0)+ 1 
        
        
    
    # To check in s 
    left = 0 
    right = 0 
    
    formed = 0 
    required = len(mpp_t)
    mpp_s = {}
    
    
    min_len = float("inf")
    min_left = 0 
    
    while right < len(s):
        
        char = s[right]
        mpp_s[char] = mpp_s.get(char,0) + 1 
        
        
        if char in mpp_t and mpp_s[char] == mpp_t[char] :
            formed += 1 

        
        while left <= right and formed == required :
            char = s[left]
            
            
            
            if right - left + 1 < min_len  :
                min_len = right - left + 1 
                min_left = left 
                
            mpp_s[char] -= 1 
            if char in mpp_t and mpp_s[char] < mpp_t[char] :
                formed -= 1
                
                
            left += 1 

        right += 1 
        
    return "" if min_len == float("inf") else s[min_left:min_left + min_len]
            
    
s = "ADOBECODEBANC"
t = "ABC"
# print(twoWin(s, t))  # Output: "BANC"



# Optimal Code 

def minWin(s,t):
    if not s or not t or len(s) < len(t) :
        return "" 
    
    
    mpp = [0] * 128 
    left, right = 0,0 
    count = len(t)
    
    min_len = float("inf")
    formed = 0 
    
    for char in t  :
        mpp[ord(char)] += 1 
        
    while right  < len(s) :
        if mpp[ord(s[right])] > 0 :
            count  -= 1 
        mpp[ord(s[right])] -= 1 
        right += 1 
        
        while count == 0 :
            if right - left  < min_len :
                formed = left 
                min_len = right - left
            
            if mpp[ord(s[left])] == 0 :
                count += 1 
            mpp[ord(s[left])] += 1 
            left += 1 
    
    return "" if min_len == float("inf") else s[formed:formed + min_len]


      
    
s = "ADOBECODEBANC"
t = "ABC"
print(minWin(s, t))  # Output: "BANC"


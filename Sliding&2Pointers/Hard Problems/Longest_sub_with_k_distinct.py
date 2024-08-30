'''
LintCode :>

Description :Given a string S, find the length of the longest substring T that contains at most k distinct characters.

Example
Example 1:

Input: S = "eceba" and k = 3
Output: 4
Explanation: T = "eceb"
Example 2:

Input: S = "WORLD" and k = 4
Output: 4
Explanation: T = "WORL" or "ORLD"

Challenge
O(n) time

'''
def longest(s,k):
    n = len(s)
    mpp = [0] * 256
    left = 0 
    e_c =  0
    length = 0 
    
    for right in range (n):
        if mpp[ord(s[right])] == 0 :
            e_c += 1 
        mpp[ord(s[right])] +=  1 
        

        while e_c > k :
            mpp[ord(s[left])] -= 1 
            if mpp[ord(s[left])]  == 0 :
                e_c -= 1 
            left += 1
            
        length  = max(length, right - left + 1)
        
    return length
    
    
    
    
     
    return length

a = "eceba"
k = 3 
print(longest(a,k))
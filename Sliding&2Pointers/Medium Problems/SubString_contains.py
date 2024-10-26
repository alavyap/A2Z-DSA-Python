'''

LeetCode :> https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/


Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1
 

Constraints:

3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.


'''

# 
def numSub(s) :
    mpp = {'a':0, 'b':0, 'c':0}
    count = 0 
    left = 0
    n = len(s)
    
    for right in range (n):
        mpp[s[right]] += 1 
        
        while mpp['a'] >0 and mpp['b'] > 0 and mpp['c']> 0  : 
            count += n - right
            
            mpp[s[left]] -= 1 
            left += 1 
    return count
    
    
a = "abcabc"
print(numSub(a))

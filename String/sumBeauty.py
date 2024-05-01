'''
LeetCode :> https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/
Coding Ninja:> https://www.naukri.com/code360/problems/sum-of-beauty-of-all-substrings_8143656?leftPanelTabValue=PROBLEM

The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
For example, the beauty of "abaacc" is 3 - 1 = 2.
Given a string s, return the sum of beauty of all of its substrings.

Example :
Input: s = "aabcb"
Output: 5
Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.

'''
# TM : O(N ^3)

def beautySum(s):
    ans = 0 
    
    for i in range (len(s)):
        freq = [0] * 26
        
        for j in range (i, len(s)):
            
            freq[ord(s[j]) - ord('a')] += 1 
            
            max_f = max(x for x in freq if x != 0)
            
            min_f = min(x for x in freq if x != 0 )
            
            ans += (max_f - min_f) 
    return ans
            
# Test Run 
# print(beautySum("aabcb"))

# T:O(N^2)

def sumWithB(s):
    ans = 0 
    for i in range (len(s)):
        freq = [0] * 26
        
        for j in range (i,len(s)):
            freq[ord(s[j])  - 97] += 1
            ans += max(freq) - min(x for x in freq if x != 0)
    return ans 
    
# Test Run 

print(sumWithB("aabcb"))
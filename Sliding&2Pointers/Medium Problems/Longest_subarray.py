'''
LeetCode :> https://leetcode.com/problems/longest-substring-without-repeating-characters/description/


Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''

# Variable Window
def lengthOfLongestSubstring(self, s: str) -> int:
    sliding_window = {} 
    max_len = 0 
    left_pointer = 0 
    string_len = len(s)


    for right_pointer in range (string_len) :
        character = s[right_pointer]

        if character in sliding_window and sliding_window[character] >= left_pointer : 
            left_pointer = sliding_window[character] + 1

        sliding_window[character] = right_pointer
        max_len = max(max_len, right_pointer - left_pointer + 1 )
    return max_len
             
             
             
# Space Complexity : O(1) ::> Optimal Apporach 
def length(s):
    mpp = [-1] *256
    
    left_p = 0 
    right_p = 0 
    n = len(s)
    length = 0 
    
    while right_p < n :
        if mpp[ord(s[right_p])] != -1 :
            left_p = max(mpp[ord(s[right_p])] + 1 , left_p)
            
        mpp[ord(s[right_p])] = right_p 
        
        length = max(length, right_p - left_p + 1)
        right_p += 1 
    return length
        
        
    
    
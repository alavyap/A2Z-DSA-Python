'''
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "pwwkew"
Output: 3

Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring
'''

def noRepeat(arr):
    n = len(arr)
    # to store the last index of each character
    char_count = {}
    left = 0
    max_length = 0
    
    for right in range (n):
        # check if the current character is repeated and adjust the window  accordingly 
        if arr[right] in char_count and char_count[arr[right]] >= left :
            left = char_count[arr[right]] + 1
            
        # update the last index of the current character
        char_count[arr[right ]] = right
        
        # Update the maximum length 
        if max_length < (right -left + 1): 
            max_length = (right - left + 1)
            
    return max_length


# Test Run 
print(noRepeat("pwwkew")) 
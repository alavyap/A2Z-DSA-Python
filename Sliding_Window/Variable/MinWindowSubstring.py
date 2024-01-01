'''
Given two strings s and t, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"

'''
def minWindow(s,t):
    # this condition is for if there is no window that has t in s
    if not s or not t:
        return ""
    
    # Initialize Varaibles
    required_char = {}
    current_window = {}
    
    for char in t: 
        required_char[char] = required_char.get(char,0) + 1
        
    left,right = 0,0
    min_len = float('inf')
    min_window_str = ""
    
    while right < len(s):
        
        # Expand the window 
        current_window[s[right]] = current_window.get(s[right], 0) + 1
       
        # Check if the current window contains all characters of t
        while all(current_window.get(char, 0) >= count for char, count in required_char.items()):
            # Update the minium window
            current_len = (right - left + 1)
            if current_len < min_len :
                min_len = current_len
                min_window_str = s[left:right + 1]
            
            # Shrink the window
            current_window[s[left]] -= 1 
            if current_window[s[left]] == 0:
                del current_window[s[left]] 
            left += 1
            
        # Move the right pointer to expand the window    
        right += 1
     
    return min_window_str
 

# Test Run 
s = "ADOBECODEBANC"
t = "ABC"
result1 = minWindow(s, t)
print(result1)  # Output: "BANC"

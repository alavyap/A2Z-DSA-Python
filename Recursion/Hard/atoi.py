'''
LeetCode :> https://leetcode.com/problems/string-to-integer-atoi/description/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.

 

Example 1:
Input: s = "42"
Output: 42
Explanation:
The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
Example 2:
Input: s = " -042"
Output: -42
Explanation:
Step 1: "   -042" (leading whitespace is read and ignored)
            ^
Step 2: "   -042" ('-' is read, so the result should be negative)
             ^
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)
             ^
Example 3:
Input: s = "1337c0d3"
Output: 1337
Explanation:
Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         ^
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
             ^
Example 4:
Input: s = "0-1"
Output: 0
Explanation:
Step 1: "0-1" (no characters read because there is no leading whitespace)
         ^
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)
          ^
Example 5:
Input: s = "words and 987"
Output: 0
Explanation:
Reading stops at the first non-digit character 'w'.

 

'''

# without Recursion 
def atoi(s):
    s = s.lstrip() 
    
    if not s :
        return 0 
    
    i = 0 
    sign = 1 
    
    if s[i] == "-":
        sign -= 1 
    elif s[i] == "+":
        sign += 1
        
    result = 0 
    
    while (i < len(s)):
        cur = s[i] 
        
        
        if not cur.isdigit():
            break 
        else :
            result = result * 10 +int(cur)
        i += 1
    
    result *= sign
    
    
    if result > (2 ** 31) - 1 :
        return 2 ** 31 -1
    
    elif result < (-2 ** 31 ): 
        return -2 ** 31
    else :
        return result
    
    
    
# With Recursion 

def atoi (s):
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    def recursive_parse(s: str, index: int, sign: int, num: int, has_started: bool) -> int:
        # Base case: if index is out of range
        if index == len(s):
            return sign * num
        
        char = s[index]
        
        # Ignore leading whitespace
        if not has_started and char == ' ':
            return recursive_parse(s, index + 1, sign, num, has_started)
        
        # Determine the sign
        if not has_started and (char == '-' or char == '+'):
            return recursive_parse(s, index + 1, -1 if char == '-' else 1, num, True)
        
        # Conversion
        if char.isdigit():
            num = num * 10 + int(char)
            has_started = True
            if sign * num < INT_MIN:
                return INT_MIN
            if sign * num > INT_MAX:
                return INT_MAX
            return recursive_parse(s, index + 1, sign, num, has_started)
        
        # Non-digit character or end of string
        if not char.isdigit() or has_started:
            return sign * num
        
        return recursive_parse(s, index + 1, sign, num, has_started)
    
    return recursive_parse(s, 0, 1, 0, False)

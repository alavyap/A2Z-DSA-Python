'''
Coding Ninja :> https://www.naukri.com/code360/problems/implement-atoi-function_981270
LeetCode :>  https://leetcode.com/problems/string-to-integer-atoi/description/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
The algorithm for myAtoi(string s) is as follows:
Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Note:
Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits. 

Example :
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
'''


def atoi (s):
    # This will remove the white spaces from the left side 
    s = s.lstrip()
    
    # If nothing is there in the string 
    if not s :
        return 0 
    
    i = 0 
    
    # This will look for positive or negative 
    sign = 1 
    
    # Checking if the number is positve or negative 
    if s[i] == "+":
        i += 1 
    elif s[i] == "-":
        i +=1 
        sign = -1 
        
    # This will store the output  
    result = 0 
    
    # Iterating over the string to get the numbers 
    while (i <len(s)):
        cur = s[i] 
        
        if not cur.isdigit() :
            break 
        else :
            result = result * 10 + int(cur)
        i += 1 
        
    
    # Adding the sign with result  
    result *= sign
        
    # Checking if the result in between (-2 **31 to 2 ** 31 -1)
    if result > (2 ** 31) -1 :
        return (2 ** 31) -1 
    elif result <= (-2 **31) :
        return (-2 ** 31)
    else :
        return result 
    
    
    
# Test Run 
print (atoi("dfdsfsdf42 "))
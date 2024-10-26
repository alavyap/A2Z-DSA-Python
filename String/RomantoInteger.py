'''
Coding Ninja :> https://www.naukri.com/code360/problems/roman-numeral-to-integer_981308
LeetCode :> https://leetcode.com/problems/roman-to-integer/description/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Example :
Input: s = "III"
Output: 3
Explanation: III = 3.

'''
# Better Approach

def romanInteger(s):
    valuesRI = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
        }
    integer = 0 
    s = s.upper()
    s = s.replace ("IV", "IIII").replace("IX", "VIIII")
    s = s.replace ("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace ("CD", "CCCC").replace("CM", "DCCCC")
    
    for char in s :
        integer += valuesRI[char]
    return integer
    
    
# Test Run 
# print(romanInteger("MCMXCIv"))
    
# Optimal Approach

def integerRoman (s):
    r = {"I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000}
    
    res = 0 
    s = s.upper()
    for i in range (len(s)):
        if (i + 1) < len(s) and r[s[i]] < r[s[i+1]]:
            res -= r[s[i]]
        else :
            res += r[s[i]]
            
    return res

# Test Run 
print(romanInteger("MCMXCIv"))
    
''' 
LeetCode :> https://leetcode.com/problems/count-good-numbers/description/

A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).
For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.
A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

Example :
Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".

Example :
Input: n = 50
Output: 564908303

'''

# Brute Force 
def count(n):
    good,x = 5 **(n %2), 4 * 5
    
    for i in range (n // 2):
        good = good * x % (10 ** 9 +7)
    return good

# Using Recursion
def countRe(n):
    MOD = (10 ** 9+ 7 )
    def count (power,x):
        if power == 0 :
            return 1 
        elif  power % 2 == 0 :
            return count(power // 2 , x *x % MOD)
        
        return x *count(power - 1 , x ) % MOD
    
    return 5 ** (n %2) * count(n// 2, 4 *5) % MOD
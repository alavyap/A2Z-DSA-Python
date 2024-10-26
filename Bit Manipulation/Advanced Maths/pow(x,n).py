'''
LeetCode:> https://leetcode.com/problems/powx-n/description/


Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104

'''

def maths(x,n):
    ans = 1.0 
    nn = n 
    if n <0 :
        nn = -1 * nn 
    while nn :
        if nn % 2  :
            ans *=  x
            nn -= 1 

        else :
            x *= x
            nn = nn // 2
    if n < 0 : 
        ans = 1.0 /ans 
    return ans 
    
    
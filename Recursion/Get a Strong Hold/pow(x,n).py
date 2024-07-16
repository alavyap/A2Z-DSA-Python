'''
LeetCode :> https://leetcode.com/problems/powx-n/description/

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
Example :
Input: x = 2.00000, n = 10
Output: 1024.00000

'''

# Brute Force 
def myPow(x,n):
    return (x**n)


def power(x,n):
    ans = 1.0 
    for i in range (n):
        ans = ans * x
    return ans


# Optimal Approach 
def pow(x,n):
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
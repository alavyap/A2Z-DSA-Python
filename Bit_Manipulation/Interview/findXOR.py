'''
GFG :> https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1

You are given two integers L and R, your task is to find the XOR of elements of the range [L, R].

Example:
Input: 
L = 4, R = 8 
Output:
8 
Explanation:
4 ^ 5 ^ 6 ^ 7 ^ 8 = 8
Your Task:

Your task is to complete the function findXOR() which takes two integers l and r and returns the XOR of numbers from l to r.

Expected Time Complexity: O(1).

Expected Auxiliary Space: O(1).

Constraints:

1<=l<=r<=109

'''
# Brute Force  Time :> O(N)
def bit_manipulation(a,b):
    # ans  = b
    for i in range (a,b):
        b = b ^ i
    #    ans = ans ^ i
    
    return b



# Optimal Code 

def bits_mani(l,r):
    return x_o_r(r) ^ x_o_r(l-1)

def x_o_r(n):
    if n % 4 == 0 :
        return n 
    elif n % 4 == 1:
        return 1 
    elif n % 4 == 2 :
        return n + 1 
    else : #n %4 == 3 
        return 0  


# Test Run 
print(bits_mani(4,8))
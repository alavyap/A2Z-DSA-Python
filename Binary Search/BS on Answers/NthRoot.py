'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/nth-root-of-m_1062679

Problem Statement: Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M.
If the 'nth root is not an integer, return -1.

Example 1:
Input Format: N = 3, M = 27
Result: 3
Explanation: The cube root of 27 is equal to 3.

Example 2:
Input Format: N = 4, M = 69
Result: -1
Explanation: The 4th root of 69 does not exist. So, the answer is -1.
'''

# Brute Force 
def brute (n,m):
    for i in range (1, m+1):
        ans = func(i,n)
        if ans == m :
            return i 
        elif (ans > m):
            break 
    return -1 

# Helper Function    
def func (i,exp):
    ans =  1 
    base = i 
    
    while (exp > 0) :
        if exp % 2 :
            exp -= 1 
            ans = ans * base 
            
        else :
            exp //=  2
            base = base * base 
            
    return ans   
# Test Run 
# print (brute(9 ,1953125))
    
    
# Optimal Approach 
def optimal (n,m):
    low = 1 
    high = m 
    
    
    while (low <= high):
        mid = (low + high) // 2 
        
        ans = Ofunc(mid,n,m)
        
        if ans == 1 :
            return mid 
        if ans == 0 :
            
            low = mid +1 
        else: 
            high = mid -1    
    return -1 

# Helper Function 
def Ofunc(mid,n,m):
    ans = 1 
    for i in range (1, n+1):
        ans *= mid 
        
        if ans >m :
            return 2 
    if ans == m :
        return 1 
    return 0

# Test Run 
print (optimal(9 ,1953125))


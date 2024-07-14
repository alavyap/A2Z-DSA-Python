'''
LeetCode :>  https://leetcode.com/problems/count-primes/description/

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0



'''
# Brute Force 
def bits (n):
    def isPrime(n):
        for i in range (2,int(n **0.5)+1):
            if n%i ==0 :
                return False
        return True
    
    
    ans = []
    
    for i in range(2,n):
        if (isPrime(i)):
           ans.append(i)
    return ans
            
        
    
    return res 


# Test Run 
print(bits(10))

# Better Approach 
def prime(n):
    truth = [True]*n 
    
    if (n < 2 ):
        return 0 
    
    truth[0],truth[1] = False,False
    i = 2 
    while (i < n):
        if (truth[i] == True) :
            for j in range (i ** 2, n ,i ):
                truth[j] = False
        i += 1 
    return truth.count(True)


# Better Solution >> 2 
def prime(n):
    truth = [True]*n 
    
    if (n < 2 ):
        return 0 
    
    truth[0],truth[1] = False,False
    i = 2 
    
    while (i*i < n):
        if (truth[i] == True) :
            for j in range (i ** i, n ,i ):
                truth[j] = False
        i += 1 
    return truth.count(True)

# Optimal  Approach 


def bits (n):
    
    store = [True] * n
    
    if n <= 2 :
        return 0 
    
    store[0] = store[1] = False
    
    for i in range (2 , int(n ** 0.5)+ 1 ):
        if store[i] :
            for j in range (i **2,n,i):
                store[j] = False 
    return sum(store)
'''
GFG :> https://www.geeksforgeeks.org/problems/prime-factorization-using-sieve/1

You are given a positive number N. Using the concept of Sieve, compute its prime factorisation.

Example:

Input: 
N = 12246
Output: 
2 3 13 157
Explanation: 
2*3*13*157 = 12246 = N.
Your Task:

Comple the function findPrimeFactors(), which takes a positive number N as input and returns a vector consisting of prime factors. You should implement Sieve algorithm to solve this problem.

 

Expected Time Complexity: O(Nlog(log(N)).

Expected Auxiliary Space: O(N).

Constraints:

1<=N<=2*105


'''

# Brute Force 
def find(atmax):
    res = [] 
    is_poss = [True] * (atmax + 1 )
    is_poss[0] = is_poss[1] = False
    
    for num in range (2 ,atmax+ 1):
        if is_poss[num]:
            res.append(num)
            for multiple in range (num * num, atmax+ 1, num):
                is_poss[multiple] = False
    return res
 
def main(N):
    ans = []
    atmax = int(N **0.5)+1
    poss = find(atmax)
    
    for p in poss :
        while N % p == 0 :
            if p not in ans :
                ans.append(p)
            N //= p 
            
    if N > 1 :
        ans.append(N)
    
    return ans 
# Test Run 
print(main(12246))

# Accepted Code 
from math import sqrt
def sieve(self):
        N = 2*(10**5)
        self.prime = [i for i in range(N + 1)]
        root = int(sqrt(N))
        for i in range(2, root + 1):
            if self.prime[i] == i:
                for j in range(i * i, N + 1, i):
                    if self.prime[j] == j:
                        self.prime[j] = i
def findPrimeFactors(self, N):
    # Code here
    ans = []
    while N > 1:
        ans.append(self.prime[N])
        N //= self.prime[N]
        
    return ans
        

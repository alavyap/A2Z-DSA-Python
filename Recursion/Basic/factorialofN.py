'''
Given a number X,  print its factorial.
This is Striver Sheet Code

'''
def factorial(n):
    if n ==0:
        return 1
    return n *factorial(n-1)
    
# Test Run
# factorial(5)
# print(factorial(3))


'''
Coding Ninja
You are given an integer 'n'.
Your task is to return a sorted array (in increasing order) containing all the factorial numbers which are less than or equal to 'n'.
The factorial number is a factorial of a positive integer,like 24 is a factorial number, as it is factorial of 4
'''

from typing import *

def factorialNumbers(n: int,ans = []) -> List[int]:
    # Write your code here
    def get_fact(n: int) -> int:
        if ( n<=1):
            return 1
        return n * get_fact(n-1)
    
    for i in range (1,n+1):
        i = get_fact(i)
        if(i <= n):
            ans.append(i)
        else:
            break
        
    return ans


# Test Run 
print(factorialNumbers(7))  # Exp Output : [1,2,6]
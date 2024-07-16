'''
Coding Ninja
Given an integer N. Print the Fibonacci series up to the Nth term.

'''
from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    # Write your code here
    ans =[]
    fibonacci(n,ans)
    return ans
    
    
    
def fibonacci (n,ans):
    if n <= 1:
        return ans.append(0)
    f1,f2 = 0,1
    for i in range(n):
        ans.append(f1)
        f1,f2 =f2, f1 + f2
    
  
    
  
    
#Test Run
print(generateFibonacciNumbers(3))
# generateFibonacciNumbers(5)


# LeetCode Fibonacci Problem


def fib(n) :
    if n <= 1 :
        # return 0
        return n
    # elif n == 1:
    #     return 1

    a , b = 0 , 1
    for _ in range(2 , n+1):
        a , b = b , a + b
    return b
            

# Test Run
print(fib(4))
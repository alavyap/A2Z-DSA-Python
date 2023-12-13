'''
Given an integer N. Print the Fibonacci series up to the Nth term.

'''
from typing import List

def generateFibonacciNumbers(n: int,ans=[]) -> List[int]: 
    # Write your code here
    if n <= 1 :
        return 0
    # elif n ==1 :
    #     return 1
    f1 = 0
    f2 = 1
    for i in range (1, n+1):
        ans.append(f1)
        i = f1 + f2
        f1 =f2
        f2 = i
    return ans

    
#Test Run
print(generateFibonacciNumbers(5))


# Unsolved 

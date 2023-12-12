'''
Given a number X,  print its factorial.
This is Striver Sheet Code

'''
def factorial(n):
    if n ==0:
        return 1
    return n *factorial(n-1)
    
# Test Run
factorial(5)
# print(factorial(5))


'''
Coding Ninja
You are given an integer 'n'.
Your task is to return a sorted array (in increasing order) containing all the factorial numbers which are less than or equal to 'n'.
The factorial number is a factorial of a positive integer,like 24 is a factorial number, as it is factorial of 4
'''
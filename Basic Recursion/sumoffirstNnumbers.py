'''
Problem statement: Given a number 'N', find out the sum of the first N natural numbers.
'''

def sumFirstN(n: int) -> int:
    # Write your code here.
    if n <=0:
        return
    return (n *(n+1)//2)
    
# Test the function
print(sumFirstN(5))


# Using loop and recursion we can also solve this problem.

def sum (n):
    sum = 0
    for i in range (1,n+1):
        sum += i
    print(sum)
sum(5)



# basic recursion method 
def sum (n):
    if n==0:
        return 0
    return n + sum(n-1)

print(sum(5))
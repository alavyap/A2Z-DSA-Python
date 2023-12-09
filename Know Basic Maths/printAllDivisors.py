'''

You are given an integer 'n'. Find the sum of all the divisors for all 'i' from 1 to n.
Example:    Input is n =5 
            Output is 1 + (1+2) + (1+3) +(1+2+4) +(1+5) = 21
Write the code in python with keeping the time complexity of the code in O(sqrt('n')).

'''

# Coding Ninja
n = int(input())
sum = 0

'''
# This is correct but exceeds the time constrains allowed in the coding ninja studio console

for i in range (1, n+1):
    for j in range (1,i+1):
        if (i %j ==0):
            sum += j
print(sum) 
# return (sum) 
'''


# Striver Question Brute Force to find the divisor of a number from 1 to n
'''
n = int(input())
for i in range (1, n+1):
    if (n %i ==0):
        print(i, end=" ")
print()
    
'''

# the code down below is not in time complexity of O(sqrt(n))


for i in range (1, n+1):
    j =1
    sqrt_i = int(i ** 0.5)
    while (j <=sqrt_i):
        if (i %j ==0):
            sum += j
            if (j != i//j ):
                sum += i//j
        j += 1
print(sum)
# return(sum)



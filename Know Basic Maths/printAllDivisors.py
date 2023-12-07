'''

Given a number, print all the divisors of the number. A divisor is a number that gives the remainder as zero when divided.
Ex : Input: 5 >> Output 1 + 3 + 4 + 7 + 6 = 21


'''

# Coding Ninja

n = int(input())
sum = 0

'''
# This is correct but exceeds the time constrains allowed in the coding ninja

for i in range (1, n+1):
    for j in range (1,i+1):
        if (i %j ==0):
            sum += j
print(sum) 
# return (sum) 
'''

# question is still unsolved 
'''
# Striver Question Brute Force
n = int(input())
for i in range (1, n+1):
    if (n %i ==0):
        print(i, end=" ")
print()
    
'''
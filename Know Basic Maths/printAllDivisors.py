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
# i = 1
# while i <= n: # the code will check if the i is in n or not
#     digits = n // i #the code will divide the n with the current i so for i = 1 and n =5 the output will be 5
#     div = n // digits #here 5 will be divided by 5 as digits result was 5 
#     sum += ((div * (div + 1)) // 2 - (i * (i - 1)) // 2) * digits
#     i = div + 1
#     print (sum)
 

        
for i in range(1,n+1):
    for j in range(1,int((i **0.5))+1):
        if i%j == 0:
            sum = sum + j
            if j != (i/j):
                sum = sum + int(i/j)
print (sum)
# return sum
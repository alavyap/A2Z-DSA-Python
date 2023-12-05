'''
You are given a Number N.
The number given is a 32 bit unsinged integer.

Find the reverse of that Number? 
Ex: reverse of 12 is 805306368

The Time Complexity should be O(log(N))
'''


# '''
# This is the leetcode problem  : Reverse Integer {Medium }
x = int(input())
sign = 1
rev = 0

# To check if the integer is negative or positive  
if (x < 0):
    sign = -1
    x = abs(x)

while x != 0:
    digit = x % 10
    rev = rev *10 + digit
    x //= 10
rev  = sign * rev

# now we will check for the 32 bit limit
maxLimit = 2 ** 31 -1
minLimit = -2**31
if (rev > maxLimit  ) or (rev  < minLimit ):
    print (0)
else: 
    print(rev)
    
# '''
    
# Coding Ninja Problem

n = int(input())
binNum = '{:032b}'.format(n)
rev = int(binNum[::-1],2)
print(rev)
'''
You are given a Number N.
The number given is a 32 bit unsinged integer.

Find the reverse of that Number? 
Ex: reverse of 123 is 321

The Time Complexity should be O(log(N))
'''

n = int(input())
oN = n
rev = 0
while (n != 0):
    digit = n % 10
    rev = rev *10 + digit
    n //= 10
    
print(rev)
    
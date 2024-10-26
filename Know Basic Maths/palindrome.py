'''
Check if a given number is a palindrome or not 
Ex 151 backwards is 151 where as 123 backward is 321 

'''

# Coding Ninja Solution

# n = int(input())
# rev =  int(str(n)[::-1])

# if (rev == n):
#     print("true")
# else:
#     print("false")


# Leetcode Solution

x = int(input())
rev = 0
nN = x
while(nN > 0):
    reminder = nN % 10
    rev = rev * 10 + reminder
    nN //= 10
if(rev == x):
    print(True)
else:
    print(False)
        
        
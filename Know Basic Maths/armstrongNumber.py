'''
Armstrong Numbers are the numbers having the sum of digits raised to power no. of digits is equal to a given number.

Ex : 153 is 1^3 + 5^3 + 3^3 = 153

'''

n = int(input())
count = len(str(n))
arm = 0
newN = n
while(n != 0):
    digit = n %10
    arm += (digit ** count)
    n //= 10
    
# check if the number is armstrong
if(newN == arm):
    print("true")
else:
    print("false")
    
# Test Run 

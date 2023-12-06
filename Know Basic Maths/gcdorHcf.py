'''
GCD : Greatest Common Divisor // HCF: Highest Common Divisor 

Ex :GDC or HCF of 12 and 9 is 3
 
'''

n = int(input())
m = int(input())
gcd =1

for i in range (1,min(n,m)+1):
    if(n % i == 0 and m % i == 0):
        gcd = i
print(gcd)
   
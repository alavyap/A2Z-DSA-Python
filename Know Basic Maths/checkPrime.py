'''
Given a number, check whether it is prime or not.
A prime number is a natural number that is only divisible by 1 and by itself.
Ex: 2,3,5,7,9,11
'''

n = int(input())
count =0
for i in range (1, n+1):
    if(n%i ==0 and n %n ==0):
        count +=1
    else:
        pass
if (count ==2 or n ==1):
    print("YES")
else:
    print("NO")
    
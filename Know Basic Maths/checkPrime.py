'''
Given a number, check whether it is prime or not.
A prime number is a natural number that is only divisible by 1 and by itself.
Ex: 2,3,5,7,9,11
'''

n = int(input())
count =0
'''
# brute force
for i in range (1, n+1):
    if(n%i ==0 and n %n ==0):
        count +=1
    else:
        pass
if (count ==2 or n ==1):
    print("YES")
else:
    print("NO")
    
'''
# the time complexity is O(sqrt('n')) for this code

sqrt_n = int(n**0.5)
for i in range (1, (sqrt_n+1)):
    if(n %i ==0):
        count += 1
        if(i != n //i):
            count += 1

# checking if the condition is meet or not 
if (count ==2):
    print("YES")
else:
    print("NO")            
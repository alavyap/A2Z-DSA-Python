'''
Check if a given number is a palindrome or not 
Ex 151 backwards is 151 where as 123 backward is 321 

'''
n = int(input())
rev =  int(str(n)[::-1])

if (rev == n):
    print("true")
else:
    print("false")
print(rev)
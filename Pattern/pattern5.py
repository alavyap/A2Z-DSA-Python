'''
Input Format: N = 6
Result:
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 

'''

n = int(input())
for i in range (n):
    for j in range ((n)-i):
        print("*",end= " ")
    print()
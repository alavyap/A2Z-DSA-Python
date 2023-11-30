'''
Input Format: N = 6
Result:   
1          1
12        21
12       321
1234    4321
12345  54321
123456654321

'''

n = int(input())

for i in range (1,n+1):
    for j in range (1,i+1):
        print(j,end=" ")
        
    for k in range (2*(n - 1)):
        print(" ",end="")
    
    for l in range (i,0,-1):
        print(l,end=" ")
    print()
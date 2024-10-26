'''
Input Format: N = 6
Result:   
A B C D E F
A B C D E 
A B C D
A B C
A B
A

'''

n = int(input())
for i in range (n):
    for j in range (n-i):
        print ( chr(ord("A") + j),end = " ")
    print()
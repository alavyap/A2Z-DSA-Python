'''
Input Format: N = 6
Result:   
A 
B B
C C C
D D D D
E E E E E
F F F F F F

'''

n = int(input())

for i in range (n):
    for j in range (i+1):
        print(chr(ord("A")+ i) , end=" ")
    print()
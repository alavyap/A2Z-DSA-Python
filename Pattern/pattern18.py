'''
Input Format: N = 6
Result:   
F
E F
D E F
C D E F
B C D E F
A B C D E F

'''

n = int(input())
for i in range (n):
    ch= chr(ord("A") + n-i-1)
    for j in range (i+1):    
        print(chr(ord(ch) + j), end=" ")
    print()
    
    
    

'''
But the coding ninja studio has a different pattern which is different from the A2Z Sheet 

Input Format N = 6
Result:
F
F E
F E D
F E D C
F E D C B
F E D C B A

'''

for i in range (n):
    ch= chr(ord("A") + n-1)
    for j in range (i+1):
        print(chr(ord(ch)-j),end=" ")
    print()
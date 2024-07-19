'''

Input Format: N = 6
Result:   
A
A B
A B C
A B C D
A B C D E
A B C D E F

'''

n =int(input())
for i in range (n):
    for j in range (i+1):
        print(chr(ord("A") + j),end=" ")
    print()
    
    
# Should have a understanding of ASCII values.
'''
Input Format: N = 6
Result:   
     *
     **
     *** 
     ****
     *****
     ******  
     *****
     ****
     ***    
     **
     *

'''

n = int(input())

for i in range (n):
    for j in range (i+1):
        print("*",end="")
    print()

for a in range (n):
    for b in range (n-a-1):
        print("*",end="")
    print()
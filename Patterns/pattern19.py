'''
Input Format: N = 6
Result:   
************
*****  *****
****    ****
***      ***
**        **
*          *
*          *
**        **
***      ***
****    ****
*****  *****
************

'''

n = int(input())

iniS = 0
for i in range (n):
    for j in range (1, n-i +1):
        print("*",end=" ")
        
    for s in range (iniS):
        print(" ",end="")
    
    for j in range (1, n-i+1):
        print("*",end=" ")
    iniS  += 2
    print()
    
    
# Lower Half 
iniS = 2 * n-2
for i in range (1,n+1):
    for j in range (1,i+1):
        print("*",end=" ")
    
    for s in range (iniS):
        print(" ",end="")
        
    for j in range (1, i+1):
        print("*",end=" ")
        
    iniS -=2
    print()    
'''

Input Format: N = 6
Result:   
*          *
**        **
***      ***
****    ****
*****  *****
************
*****  *****
****    ****
***      ***
**        **
*          *

'''

n = int(input())

iniS = 2 * n-2
for i in range (1,2*n):
    if i <= n :
        stars = i 
    else:
        stars = 2 * n - i
    for j in range (1,stars +1):
        print("*",end="")
    
    for s in range (1,iniS +1):
        print (" ", end= "")
    
    for j in range (1, stars + 1):
        print("*",end="")
    print()
    
    if (i<n):
        iniS -=2
    else:
        iniS +=2


 
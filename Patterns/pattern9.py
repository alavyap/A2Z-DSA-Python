'''
Input Format: N = 6
Result:   
     *
    ***
   ***** 
  *******
 *********
***********  
***********
 *********
  *******
   ***** 
    ***    
     *
'''

n = int(input())
for i in range (n):
    for j in range (n-i-1):
        print(" ",end="")
    for k in range (2*i + 1):
        print("*",end= "")
    print()
    
    
for a in range (n):
    # this is for the inverse pattern
    for z in range (a):
        print (" ", end ="")
    for x in range (2*n - (2*a +1)):
        print("*",end="")
    for z in range (a):
        print (" ", end ="")
        
    print()
    

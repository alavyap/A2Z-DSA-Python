'''
Input Format: N = 6
Result:     
***********
 *********
  *******
   ***** 
    ***    
     *
'''
n = int(input())
for i in range (n):
    for k in range (i):
        print(" ",end= "")
    for j in range ( 2*n -(2*i +1)):
        print("*",end= "")
    for k in range (i):
        print(" ",end= "")
    print()
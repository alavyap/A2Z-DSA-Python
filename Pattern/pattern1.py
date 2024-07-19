'''
Input = 3 
Output =  * * * 
          * * *  
          * * *

'''     

n = int(input())
for i in range (n):
    for j in range (n):
        print ("*", end= " ")
    print()
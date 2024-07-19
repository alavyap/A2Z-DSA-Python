'''
Input Format: N = 6
Result:   
     A     
    ABA    
   ABCBA   
  ABCDCBA  
 ABCDEDCBA 
ABCDEFEDCBA

'''

n = int(input())
for i in range (n):
    for k in range (n-i-1):
        print(" ",end="" )        
    ch = 'A'
    breakpoint = (2*i+1) // 2
    for j in range (1,2*i+2):
        print(ch,end=" ")
        if (j <= breakpoint):
            ch = chr(ord(ch) + 1)
        else: 
            ch = chr(ord(ch) - 1)
    for k in range (n-i-1):
        print(" ",end="" )
    print()
'''
Input Format: N = 6
Result:
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1

'''

n = int(input())
for i in range (n):
    for j in range (1, n-i+1):
        print(j,end= " ")
    print()

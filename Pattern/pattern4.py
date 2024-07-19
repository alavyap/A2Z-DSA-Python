'''
        Input Format: N = 6
        Result:
        1
        2 2
        3 3 3
        4 4 4 4
        5 5 5 5 5
        6 6 6 6 6 6
'''

n = int(input())
for i in range (n+1):
    for j in range (1,i+1):
        print(i,end= " ")
    print()
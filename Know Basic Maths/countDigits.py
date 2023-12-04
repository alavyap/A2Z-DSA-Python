'''
You are given N number.
Find the number of digits of "n" that evenly divides "n".

The time complexity should be O(log (N))

'''

n = int(input())

# My Approach

count = 0
d = []
oN = n
while (n >0):
    ld = n %10
    d.append(ld)
    n = n //10    
for i in  (d):
    if ((i != 0) and (oN % i == 0)):
        count += 1
print(count)
# return (count)


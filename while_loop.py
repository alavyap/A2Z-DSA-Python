#  Example 1 
n = 5 
factorial = 1

while (n > 0):
    factorial *= n
    n -= 1
    
print ("Factorial of 5 is: {}".format(factorial))

# ---------------------------------------------------------------------------------

# Example 2
numbers = [1,2,3,4,5,6,7,8,9]
target = 6

for num in numbers:
    if (target == num ):
        print("Target found: {}".format(num))
        break
    print("Checking: {}".format(num))
    
for num in numbers :
    if (num %2 ==0):
        continue
    print("Odd numbers: {}".format(num))

# -----------------------------------------------------------------------

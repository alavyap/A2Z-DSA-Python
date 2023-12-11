'''
Problem: Print your Name N times using recursion
Without Using any loop

'''

i =1
def printNtimes(n: int) -> None:
    global i
    if (i >n):
        return
    else:
        print("Coding Ninjas",end=" ")
        i += 1
        printNtimes(n)
        
        
# Test Run
# printNtimes(4)


# Another Approach : More Organized Way
def print_name(n: int) -> None:
    if n <= 0:
        return
    print("Coding Ninja",end=" ")
    print_name(n-1)
    
# Test Run
print_name(4)
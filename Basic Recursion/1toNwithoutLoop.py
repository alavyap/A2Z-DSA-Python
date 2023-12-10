'''
You are given an interger 'n'
Return an array containing integers from 1 to n (in increasing order) without using loops.
Coding Ninja requires only in C++ but this is how you can get the same result in python

'''

i = 1

def give_array(n):
    global i

    # Base Condition
    if i == n+1:
        return

    print(i,end= " ")
    
    # Count Incremented
    i += 1
    give_array(n)

# Test Run
give_array(10)

# here i an not using  any loop 


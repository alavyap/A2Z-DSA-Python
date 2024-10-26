'''
Assume, we are given an array: [2, 5, 16, 28, 139]. Here, we can apply array hashing, and to use that, we need to create an array of size 140. 
Now, what to do if we are given a constraint that we cannot use an array whose length is greater than 10?
'''

def divisionMethod (n,a):
    hash_table = [0] * 10
    for i in range (len(a)):
        hash_table[a[i] %10] += 1 
        
    print(hash_table[n%10])
    
    
divisionMethod(139,[2,138,149,169,179,189,199])

# Here we will have a case where 5 numbers have same mod 
# To solve this we can use linear chaining. That Case will be called as a Collision.
# which will store all the elements of same index in a linked list at that index 
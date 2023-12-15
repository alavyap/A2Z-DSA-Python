'''
                                            Hashing
arr = [1,2,1,3,2] {1:2, 2:2, 3:1 }
We have to find the number of times a single element has been repeated 
'''


# Brute Force Approach
# The below problem is done using basic for loop
def hashing(n,a):
    count = 0
    for i in range (len(a)):
        if n==a[i]:
            count+=1
    return ("{} : {}".format(n,count))


# print(hashing(3,[1,2,1,3,2]))

# This is not the correct way to solve this question as it will take more then 100 sec to execute so we need to use hashing, 


# Character  arr= [a,b,a,a,c]
# Brute Force Approach
def chrHashing(n,a):
    count = 0
    for i in range (len(a)):
        if n == a[i]:
            count += 1
    return ("{}: {}".format(n,count))
    
    
# Test Run
print(chrHashing('a',['a','b','a','a','c']))
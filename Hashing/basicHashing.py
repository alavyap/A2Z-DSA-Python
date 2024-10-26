
# To able to solve hashing in python you need to know dictionary and it's operations 
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


print(hashing(3,[1,2,1,3,2]))



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

# This is not the correct way to solve this question as it will take more then 100 sec to execute so we need to use hashing, 

'''
# Using Hashing  to find repeated number
n = int(input())
arrN = [int(input()) for _ in range (n)]

# Pre computing
hash_table = [0] * 13
for i in range (n):
     if 0 <= arrN[i] <= 12:
        hash_table[arrN[i]] += 1
f = int(input())
while (f >0):
    number = int(input())
    
    if 0 <= number <= 12:
        print(hash_table[number])
    f -= 1
'''
# Hashing on Number
def hash_number(n,a):
    hash_table = [0] * 13
    for i in range (len(a)):
        hash_table[a[i]] += 1
          
    print(hash_table[n])
                
hash_number(1,[1,2,1,3,2])
 
# Hashing on characters 

def char_Hashing(n,a):
    hash_table = [0] * 256
    for i in range (len(a)):
        hash_table[ord(a[i])] += 1
    
    print(hash_table[ord(n)])
           
char_Hashing('A',['a','b','a','a','c','A','A','C','B'])


'''
# In C++ we use map for storing the values in Hashing, where as we use dictionary to store the data of Hashing in Python.
# The below codes are the example of hashing using dictionary.
'''

def dict_hashNumber(n,a):
    dict = {}
    for i in range (len(a)):
        if a[i] in dict:
            dict[a[i]] += 1
        else:
            dict[a[i]]=1
            
    print(dict.get(n,0))
        
# Test Run
dict_hashNumber(1,[1,2,1,4,3,1])


# Characters 
def  dict_hashChar(n,a):
    dictChar= {}
    for i in range (len(a)):
        if a[i] in dictChar:
            dictChar[a[i]] += 1
            
        else:
            dictChar[a[i]] = 1
            
    print(dictChar.get(n,0))
    
# Test Run
dict_hashChar('A',['a','b','a','a','c','A','A','C','B'])



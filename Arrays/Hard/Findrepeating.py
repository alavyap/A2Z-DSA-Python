'''
Coding Ninja : > https://www.codingninjas.com/studio/problems/missing-and-repeating-numbers_6828164?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse

Problem Statement: You are given a read-only array of N integers with values also in the range [1, N] both inclusive. 
Each integer appears exactly once except A which appears twice and B which is missing. 
The task is to find the repeating and missing numbers A and B where A repeats twice and B is missing.

Example :
Input Format:  array[] = {3,1,2,5,3}
Result: {3,4)
Explanation: A = 3 , B = 4 
Since 3 is appearing twice and 4 is missing
'''

# Brute Force 
def findmissing (arr):
    n = len(arr)
    store = {} 
    repeat = 0
    for i in range (n):
        if arr[i] in store :
            store[arr[i]] +=1 
        else :
            store[arr[i]] = 1 
    for k,v in store.items() :
        if v == 2 :
            repeat = k
        
    # For missing 
    aSum = (n * (n+1)) //2 
    aSet = set(arr)
    arrSum = 0
    for ele in aSet :
        arrSum  += ele
    miss = aSum -  arrSum    
    # return ans
    return [repeat,miss]

# Test Run 
# print (findmissing([3,1,2,5,3]))

# Brute Force > From striver sheet 
def bf(arr):
    n = len(arr)
    repeat  = -1 
    miss = -1
    
    for i in range (1,n+1):
        count = 0 
        for j in range (n):
            if arr[j] == i : 
                count += 1 
                
        if count  == 2 :
            repeat = i 
            
        elif count == 0 :
            miss = i 
            
        if repeat != -1 and miss != -1 :
            break 
    
    return [repeat,miss]
        
# Test Run 
# print (bf([3,1,2,5,3]))

# Better Approch 
def ba(arr):
    n = len(arr)
    repeat = -1 
    miss = -1 
    hashArr = [0] * (n+1)
    for i in range (n):
        hashArr[arr[i]] += 1
        
    for j in range (1,n+1):
        if hashArr[j] == 2 :
            repeat = j
        elif hashArr[j] == 0 :
            miss = j 
        
        if repeat != -1 and miss != -1 :
            break
        
    return [repeat,miss]
        
# Test Run 
# print (ba([3,1,2,5,3]))


# Optimal Approach >> Using Basic Maths 
def opMath(arr):
    n = len(arr)
    sR = (n * (n+1))//2 
    sRs = (n*(n+1)* (2*n +1)) //6
    
    s = 0 
    ss = 0 
    
    for i in range (n):
        s += arr[i] 
        ss += arr[i] * arr[i] 
        
        
    equ1 = s- sR
    equ2 = ss -sRs 
    
    
    equ2 = equ2 //equ1 
    
    repeat = (equ1 +equ2) // 2 
    miss = repeat - equ1
    
    return (repeat,miss)


# Test Run 
print (opMath([3,1,2,5,3]))
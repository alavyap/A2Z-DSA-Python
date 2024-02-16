'''
Coding Ninja : > https://www.codingninjas.com/studio/problems/subarrays-with-xor-k_6826258?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
InterView Bit  :>  https://www.interviewbit.com/problems/subarray-with-given-xor/

Problem Statement: Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.
Example :
Input Format: A = [4, 2, 2, 6, 4] , k = 6
Result: 4
Explanation: The subarrays having XOR of their elements as 6 are  [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
'''
# Brute Force 
from collections import defaultdict



def countSubarray(arr,target):
    n = len(arr)
    count = 0 
    
    for i in range (n):
        for j in range (i,n):
            
            Xor = 0 
            for k in range (i,j+1):
                Xor = Xor ^ arr[k]
            if (Xor == target):
                count +=1 
    return count 


# Test Run 
# print(countSubarray([4,2,2,6,4],6))

# Better Approach 
def countXor(arr,target):
    n = len(arr)
    count = 0 
    for i in range (n):
        Xor = 0 
        for j in range (i,n):
            Xor = Xor ^ arr[j]
            
            if Xor == target :
                count += 1 
    return count

# Test Run 
# print(countXor([4,2,2,6,4],6))

# Optimal Approach 
def optCountSub(arr,target):
    n = len(arr)
    mpp = defaultdict(int)
    count = 0 
    Xor = 0 
    mpp[Xor] = 1
    for i in range (n):
        Xor = Xor ^ arr[i] 
        
        x = Xor ^ target  
        count += mpp[x]
        
        mpp[Xor] += 1 
    return count        


# Test Run 
print(optCountSub([4,2,2,6,4],6))


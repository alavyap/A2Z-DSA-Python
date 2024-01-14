'''
Link : 
Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array.
Example:

Input Format: N = 5, array[] = {1,2,4,5}
Result: 3
Explanation: In the given array, number 3 is missing. So, 3 is the answer.
'''

def findMissing(arr,n):
    num = []
    for i in range  (1,n+1):
        num.append(i)
        
    for j in range (n):
        if arr[j] != num[j] :
            return num[j]
    
        
# Test Run
print(findMissing([1,2,3,5],5))
    
# Optimal Approach 

def findmissing(nums,N):
    
    sum1 =  (N*(N+1)) //2
    sum2 = 0
   
    for i in range (len(nums)):
        sum2 += nums[i]
        
    return sum1 - sum2
        

# Test Run 
# print(findmissing([1,2,4,5],5))
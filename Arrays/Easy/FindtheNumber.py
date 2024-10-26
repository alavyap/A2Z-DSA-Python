'''
Link :> https://www.codingninjas.com/studio/problems/find-the-single-element_6680465?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse
Problem Statement: Given a non-empty array of integers arr, every element appears twice except for one. Find that single one.
Example:
Input Format: arr[] = {2,2,1}
Result: 1
Explanation: In this array, only the element 1 appear once and so it is the answer.
Leetcode and Coding Ninja have same questions 
'''

# In Brute force we will run 2 for loops and check if the count is 1, if so we return num
# Brute Force >> Better Than that 
def getSingleElement(arr):
    n = len(arr)
    dictCount = {} 
    
    for i in range (n):
        if arr[i] in dictCount:
            dictCount[arr[i]] += 1
        else:
            dictCount[arr[i]] = 1
    
    # To return a key or a value from a dictionary we use this for loop
    for key,value in dictCount.items():
        if value == 1 :
            return key #the complexity is O(N*log(M)) + O(M) > the M is the time for the dictionary
    
# Test Run
# print(getSingleElement([1,1,2,3,3,4,4]))


# Optimal Approach >> Use of XOR Property >> Search on Youtube for understanding it 
def singleElement(arr):
    single = 0
   
    for i in arr:
        single ^= i
    return single

'''
Two important properties of XOR are the following:

XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.
XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ←Property 2
'''
        
    
    
    
# Test Run 
print(singleElement([1,1,2,3,3,4,4]))
    
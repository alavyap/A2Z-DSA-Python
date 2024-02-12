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
    ans = []
    for i in range (n):
        if arr[i] in store :
            store[arr[i]] +=1 
        else :
            store[arr[i]] = 1 
    for k,v in store.items() :
        if v == 2 :
            ans.append(k)
        
    # For missing 
    
    return ans

# Test Run 
print (findmissing([3,1,2,5,3]))
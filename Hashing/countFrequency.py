'''
Input: arr[] = {10,5,10,15,10,5};
Output: 10  3
	    5  2
        15  1
Explanation:
            10 occurs 3 times in the array
	        5 occurs 2 times in the array
            15 occurs 1 time in the array
'''

# My Approach
def countFrequency(a):
    countN = {}
    for i in range (len(a)):
        if a[i] in countN:
            countN[a[i]] += 1
        else:
            countN[a[i]] = 1
    for keys,values in countN.items():
        print(f"{keys} {values}")
    
# countFrequency([10,5,10,15,10,5])

# Striver Approach
def countFreq(arr,n):
    visited= [False] * n
    for i in range (n):
        if (visited[i] == True):
            continue
        count = 1
        for j in range (i+1,n):
            if(arr[i] == arr[j]):
                visited[j] = True
                count += 1    
        print(arr[i], count)
        
    
# countFreq([10,5,10,15,10,5],6)


'''
# Coding Ninja 
You are given an array 'arr' of length 'n' containing integers within the range '1 to x'
There are 3 inputs  n = length of array ; x = max number in the array ; arr = the array 

'''

from typing import List

def countFrequency(n: int, m: int, edges: List[int]):
    count = {}

    for i in range(n):
        if edges[i] in count:
            count[edges[i]] += 1
        else:
            count[edges[i]] = 1
            
    result = []
    for j in range (1, n+1):
        # print(f"{j} {count.get(j,0)}") # this is for printing both the index and its coresponding value
        result.append(count.get(j,0))
    return result

# Example usage:
print(countFrequency(10,14,[11,14,8,3,12,14,1,7,4,3]))

# Leetcode Hashing Problem  1512.Number of Good Pairs
def numIdentical(m):
    count  = 0
    for i in range (len(m)):
        for j in range (i):
            if m[i] == m[j]:
                count +=1 
    print (count)
    
# numIdentical([1,1,1,1])

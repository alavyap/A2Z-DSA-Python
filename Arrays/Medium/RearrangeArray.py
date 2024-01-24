'''
Coding Ninja : > https://www.codingninjas.com/studio/problems/alternate-numbers_6783445?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode :> https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

Rearrange Array Elements by Sign
Variety-1
Problem Statement:
There's an array 'A' of size 'N' with an equal number of positive and negative elements. 
Without altering the relative order of positive and negative elements, 
you must return an array of alternately positive and negative values.

Note: Start the array with positive elements.
Example:
Input:
arr[] = {1,2,-4,-5}, N = 4
Output:
1 -4 2 -5
Explanation: 
Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.

'''
# Brute Force
def reArrange (arr,n):
    Ncount = []  
    Pcount = []
    Dis = []
    
    for i in range (n):
        if arr[i] < 0 :
            Ncount.append(arr[i])
            
        else:
            Pcount.append(arr[i])
            
    for i in range (len(Pcount)):
        # Here 2 * i will give positive index where the positive elements will be set
        arr[2*i] = Pcount[i]
    
    for i in range (len(Ncount)):
        arr[2 * i + 1] = Ncount[i]
    return arr

# Test Run 
# print(reArrange([1,2,-4,-5],4))

# Optimal Solution 
def positions(arr):
    n = len(arr)
    temp = [0] * n
    pos = 0
    neg = 1 
    
    for i in range (n):
        if arr[i] < 0 :
            temp[neg] = arr[i]
            neg += 2
        else:
            temp[pos] = arr[i]
            pos += 2
    return temp
    

# Test Run 
# print(positions([1,2,-4,-5]))

'''
Problem Statement:
There's an array 'A' of size 'N' with positive and negative elements (not necessarily equal). 
Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.
The leftover elements should be placed at the very end in the same order as in array A.

Note: Start the array with positive elements.

Examples: 

Input:
arr[] = {1,2,-4,-5,3,4}, N = 6
Output:
1 -4 2 -5 3 4

Explanation: 

Positive elements = 1,2
Negative elements = -4,-5
To maintain relative ordering, 1 must occur before 2, and -4 must occur before -5.
Leftover positive elements are 3 and 4 which are then placed at the end of the array.
'''

def extras(arr):
    n = len(arr)
    pos = []
    neg = []
    
    for i in range (n):
        if arr[i] >0 :
            pos.append(arr[i])
        else:
            neg.append(arr[i])
        
    
    if (len(pos)) < (len(neg)):
        for i in range (len(pos)):
            arr[2*i] = pos[i]
            arr[2 *i +1] = neg[i]
        
        index = len(pos) * 2
        for i in range (len(pos) - len(neg)):
            arr[index] = neg[len(pos) + i]
            index += 1
            
    else :
        for i in range (len(neg)):
            arr[2 * i] = pos[i]
            arr[2 * i + 1] = neg[i]
            
        index = len(neg) *2
        for i in range (len(pos)- len(neg)):
            arr[index] = pos[len(neg) + i ]
            index += 1
    return arr

# Test Run 
# print (extras([1,2,-4,-5,3,4]))
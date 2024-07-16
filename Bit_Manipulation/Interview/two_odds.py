'''
GFG :> https://www.geeksforgeeks.org/problems/two-numbers-with-odd-occurrences5846/1

Given an unsorted array, Arr[] of size N and that contains even number of occurrences for all numbers except two numbers. Find the two numbers in decreasing order which has odd occurrences.

Example 1:

Input:
N = 8
Arr = {4, 2, 4, 5, 2, 3, 3, 1}
Output: {5, 1} 
Explaination: 5 and 1 have odd occurrences.

Example 2:

Input:
N = 8
Arr = {1 7 5 7 5 4 7 4}
Output: {7, 1}
Explaination: 7 and 1 have odd occurrences.

Your Task:
You don't need to read input or print anything. Your task is to complete the function twoOddNum() which takes the array Arr[] and its size N as input parameters and returns the two numbers in decreasing order which have odd occurrences.


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
2 ≤ N ≤ 106
1 ≤ Arri ≤ 1012

'''

# Brute Force  
def bit (Arr,n):
    Arr.sort()
    xor = 0 
    for num in Arr :
        xor ^= num
        
    right = xor & -xor
    
    
    one = 0 
    two = 0 
    for num in Arr :
        if num & right :
            one ^= num 
        else :
            two ^= num 
    
        
    return two,one

# Test Run 
# arr = [1, 7, 5, 7, 5, 4, 7, 4]
arr =  [37, 30, 12, 12, 19, 19, 30, 19, 19, 37, 12, 2, 2, 19, 37, 2, 12, 2, 12, 19, 46, 2, 2, 2, 37, 12, 12, 37, 2, 2, 27, 19, 46, 12, 2, 37, 12, 12]
n = len(arr)
# print(bit(arr, n))


# Not Using Bit Manipulation as GFG was not accepting the code 

def not_bit(Arr,n):
    map = {}
    
    for num in Arr :
        if num in map:
            map[num] += 1 
        else :
            map[num] = 1 
    
    result = [num for num,count in map.items() if count % 2 != 0  ]
    
    if result[0] < result[1]:
        result[0],result[1] = result[1],result[0] 
        
    return result

# Test Run 
Arr =  [37, 30, 12, 12, 19, 19, 30, 19, 19, 37, 12, 2, 2, 19, 37, 2, 12, 2, 12, 19, 46, 2, 2, 2, 37, 12, 12, 37, 2, 2, 27, 19, 46, 12, 2, 37, 12, 12]
n = len(Arr)

print(not_bit(Arr,n))
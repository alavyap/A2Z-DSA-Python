'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/kth-missing-element_893215
LeetCode :> https://leetcode.com/problems/kth-missing-positive-number/description/

Problem Statement: You are given a strictly increasing array ‘vec’ and a positive integer ‘k’. Find the ‘kth’ positive integer missing from ‘vec’.

Example :
Input Format: vec[]={4,7,9,10}, k = 1
Result: 1
Explanation: The missing numbers are 1, 2, 3, 5, 6, 8, 11, 12, ……, and so on. Since 'k' is 1, the first missing element is 1.
'''

# Brute Force 
def brute(arr, k):
    n = len(arr)
    maxi = max(arr)
    mini = min(arr)
    
    ans = None  # Default value
    
    if k < mini:
        ans = solu(k, mini)
    elif k > mini and k < maxi:
        ans = solu(k, maxi)
    
    return ans 

def solu(start, end):
    store = []
    for i in range(start, end):
        store.append(i)
    return [store]

# Test Run 
print(brute([4,7,9,10],4))
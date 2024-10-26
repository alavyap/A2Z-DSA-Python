'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/aggressive-cows_1082559
LeetCode :> https://www.spoj.com/problems/AGGRCOW/

Problem Statement: You are given an array ‘arr’ of size ‘n’ which denotes the position of stalls.
You are also given an integer ‘k’ which denotes the number of aggressive cows.
You are given the task of assigning stalls to ‘k’ cows such that the minimum distance between any two of them is the maximum possible.
Find the maximum possible minimum distance.

Example :
Input Format: N = 6, k = 4, arr[] = {0,3,4,7,10,9}
Result: 3
Explanation: The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions {0, 3, 7, 10}. 
Here the distances between cows are 3, 4, and 3 respectively. We cannot make the minimum distance greater than 3 in any ways.
'''
# Brute Force 
def brute (arr,n,k):
    arr.sort()
    maxi = max(arr)
    mini = min(arr)
    limit = arr[n-1] - arr[0]
    for i in range (1, (maxi- mini)):
        if not helper(arr,i,k):
            return i-1
    return limit 

# Helper Function 
def helper(arr,dist,k):
    cntCow = 1 
    lastPlace = arr[0] 
    for i in range(1,(len(arr))):
        if arr[i] - lastPlace >= dist :
            cntCow += 1 
            lastPlace = arr[i] 
        if cntCow >= k : 
            return True 
    return False 

# Test Run 
# print(brute([0,3,4,7,10,9],6,4))

# Optimal Approach 
def optimal (arr,k):
    n = len(arr)
    arr.sort()
    
    low = 1
    high =  arr[n-1] - arr[0] 
    
    while(low <= high):
        mid = (low + high) // 2
        
        if  help(arr,mid,k):
            low = mid +1 
        else: 
            high = mid - 1 
    return high 

# Help 
def help(arr,dist,k):
    cnt = 1 
    lastP = arr[0] 
    n = len(arr)
    for i in range (1,n):
        if arr[i] - lastP >= dist :
            cnt += 1 
            lastP = arr[i] 
        if cnt >= k :
            return True
    return False  

# Test Run 
print(brute([0,3,4,7,10,9],6,4))
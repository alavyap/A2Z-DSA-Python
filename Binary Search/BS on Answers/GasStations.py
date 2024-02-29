'''
Coding Ninja :> https://www.codingninjas.com/studio/problems/minimise-max-distance_7541449
Problem Statement: You are given a sorted array ‘arr’ of length ‘n’, which contains positive integer positions of ‘n’ gas stations on the X-axis. 
You are also given an integer ‘k’. You have to place ‘k’ new gas stations on the X-axis. You can place them anywhere on the non-negative side of the X-axis, 
even on non-integer positions. Let ‘dist’ be the maximum value of the distance between adjacent gas stations after adding k new gas stations.
Find the minimum value of ‘dist’.

Note: Answers within 10^-6 of the actual answer will be accepted. For example, if the actual answer is 0.65421678124, it is okay to return 0.654216.
Our answer will be accepted if that is the same as the actual answer up to the 6th decimal place.

Example :
Input Format: N = 5, arr[] = {1,2,3,4,5}, k = 4
Result: 0.5
Explanation: One of the possible ways to place 4 gas stations is {1,1.5,2,2.5,3,3.5,4,4.5,5}. Thus the maximum difference between adjacent gas stations is 0.5. 
Hence, the value of ‘dist’ is 0.5. 
It can be shown that there is no possible way to add 4 gas stations in such a way that the value of ‘dist’ is lower than this. 
'''

# Brute Force 

def brute(arr,k):
    n = len(arr)
    howMany = [0] * (n-1)
    for gasStations in range (1,k+1):
        maxSection = -1
        maxIndex = -1 
        
        for i in range (n-1):
            diff = arr[i+1] - arr[i]
            sectionLength = diff /(howMany[i] +1)
            if sectionLength > maxSection :
                maxSection = sectionLength
                maxIndex = i 
            howMany[maxIndex] += 1
            
        
    # This is to find the min max between the gas stations
    maxAns = -1 
    for i in range (n-1):
        diff = arr[i+1] - arr[i] 
        sectionLength = diff / (howMany[i]+1)
        maxAns = max(maxAns,sectionLength)
        
    return maxAns
               
# Test Run 
# print(brute([1,2,3,4,5],4))


'''
Priority Queue: Priority queue internally uses the heap data structure. In the max heap implementation,
the first element is always the greatest of the elements it contains and the rest elements are in decreasing order.
'''

# Better Approach 
import heapq
def better (arr,k):
    n = len(arr)
    howMany = [0] * (n-1)
    pq = []
          
    for i in range (n-1):
        heapq.heappush(pq,((-1)* (arr[i+1] - arr[i]),i))
            
    for gasStations in range (1, k+1):
        tp = heapq.heappop(pq)
        secInd = tp[1]
            
        howMany[secInd] += 1 
          
        indiff = arr[secInd + 1] - arr[secInd]
          
        newSecLen = indiff / (howMany[secInd] + 1)
        heapq.heappush (pq,(newSecLen*(-1),secInd))
            
    return pq[0][0] * (-1)

# Test Run 
# print(better([1,2,3,4,5],4))

# Optimal Approach
def optimal(arr,k):
    n = len(arr)
    low = 0 
    high = 0 
    
    # Find the maximum distance :
    for i in range (n-1):
        high = max(high,arr[i+1] - arr[i] )
        
    # Apply Binary Search 
    diff = 1e-6
    
    while (high - low) > diff :
        mid = (low + high ) / 2
        
        cnt = numberOfGasStationsReq(mid, arr)
        if cnt > k :
            low = mid 
        else :
            high = mid 
    return high

# Helper Function
def numberOfGasStationsReq(dist,arr):
    n = len(arr)
    count = 0 
    for i in range (1,n):
        numberInBetween = ((arr[i] - arr[i-1]))
        count += (numberInBetween // dist)
    return count

# Test Run 
print(optimal([1,2,3,4,5],4))
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
    

# Test Run 
print(brute([1,2,3,4,5],4))
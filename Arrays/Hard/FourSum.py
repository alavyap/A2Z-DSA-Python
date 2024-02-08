'''
Coding Ninja :>  https://www.codingninjas.com/studio/problems/4sum_5713771?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
LeetCode : > https://leetcode.com/problems/4sum/
Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value.
In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.

Note:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
arr[a] + arr[b] + arr[c] + arr[d] == target

Example :
Input Format: arr[] = [1,0,-1,0,-2,2], target = 0
Result: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Explanation: We have to find unique quadruplets from the array such that the sum of those elements is equal to the target sum given that is 0. 
The result obtained is such that the sum of the quadruplets yields 0.
'''

# Brute Force 
def sumBF(arr,k):
    n = len(arr)
    
    aSet = set()
    for i in range (n):
        for j in range (i+1,n):
            for k in range (j+1,n):
                for l in range (k+1,n):
                    
                    sum =  arr[i] + arr[j]
                    sum += arr[k]
                    sum += arr[l]
                    
                    if sum == k :
                        temp =  [arr[i],arr[j],arr[k],arr[l]]
                        temp.sort() 
                        aSet.add(tuple(temp))
                        
                        
    ans = [list(t) for t in aSet]
    
    return ans 
  

# Test Run 
print (sumBF([4,3,3,4,4,2,1,2,1,1],k=9))
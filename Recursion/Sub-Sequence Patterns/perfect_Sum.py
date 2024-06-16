'''
GFG :> https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/

Given an array arr of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.
Note: Answer can be very large, so, output answer modulo 10 ** 9+7.

Example :
Input: 
N = 6
arr = [5, 2, 3, 10, 6, 8]
sum = 10
Output: 
3
Explanation: 
{5, 2, 3}, {2, 8}, {10} are possible subsets.

'''

# Recursive Approach

def perfect_Sum(arr,n,sum):
    ans = {}
    return count_sum(arr,n,sum,ans)


def count_sum(arr,n,sum, ans):
    MOD = 10 ** 9 + 7
    if sum == 0 :
        return 1 
    if n == 0 :
        return 0
    
    if (n,sum) in  ans :
        return ans[(n,sum)]
    exclude = count_sum(arr,n-1,sum,ans)
    include = 0 
    if arr[n-1] <= sum :
        include = count_sum(arr,n-1,sum - arr[n-1], sum)
        
    ans[(n,sum)] = (exclude + include) % MOD
    
    return ans[(n,sum)]
    
    
'''
Link :> https://www.naukri.com/code360/problems/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum_842494?source=youtube&campaign=striver_dp_videos&leftPanelTab=0&leftPanelTabValue=PROBLEM


You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

Return the minimum possible absolute difference.

 

Example 1:

example-1
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
Example 2:

Input: nums = [-36,36]
Output: 72
Explanation: One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
Example 3:

example-3
Input: nums = [2,-1,0,4,-2,-9]
Output: 0
Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.
 

Constraints:

1 <= n <= 15
nums.length == 2 * n
-107 <= nums[i] <= 107

'''
# Memoization
def minimumDiff(nums): 
    
    n = len(nums)
    totalSum = sum(nums)
    dp = [[-1 for _ in range (totalSum +1)] for _ in range (n)]
    
    for i in range (totalSum+1): 
        dummy = helper(n-1,i,nums,dp)
        
    mini = int(1e9)
    
    for i in range (totalSum + 1): 
        if dp[n-1][i] == True: 
            diff = abs(i - (totalSum -i))
            mini = min(mini,diff)
    return mini 

def helper(ind,target,arr,dp): 
    if target == 0 : 
        return True 
    
    if ind == 0 : 
        return arr[0] == target

    if dp[ind][target] != -1 : 
        return dp[ind][target]
    
    notTaken = helper(ind-1, target,arr,dp)
    
    taken = False
    if arr[ind] <= target: 
        taken = helper(ind-1,target - arr[ind],arr,dp)
        
    dp[ind][target] = notTaken or taken 
    return dp[ind][target]
        
# Tabulation 
def minSum(arr): 
    n = len(arr)
    
    totalSum = sum(arr)
    dp = [[False for _ in range (totalSum + 1)] for _ in range (n)]
    for i in range (n): 
        dp[i][0] = True 
        
    if arr[0] <= totalSum:
        dp[0][arr[0]] = True 
        
    for ind in range (1,n): 
        for target in range (1,totalSum+1): 
            notTaken = dp[ind-1][target]
            taken = False 
            if arr[ind] <= target: 
                taken = dp[ind-1][target - arr[ind]]
                
            dp[ind][target] = notTaken or taken
            
    mini = int(1e9)
    
    for i in range (totalSum +1): 
        if dp[n-1][i] == True: 
            diff = abs(i - (totalSum -i))
            mini = min(mini,diff)
            
    return mini



# Space Optimization 

def diffSum(arr):
    
    n = len(arr)
    totalSum = sum(arr)
    
    prev = [False] * (totalSum +1)
    prev[0] = True 
    
    if arr[0] <= totalSum: 
        prev[arr[0]] = True 
    for ind in range (1,n):
        curr = [False] * (totalSum +1)
        curr[0] = True 
        
        for target in range (1,totalSum +1): 
            notTaken = prev[target]
            
            taken = prev[target - arr[ind]] if arr[ind] <= target else False 
            
            curr[target] = notTaken or taken 
            
        prev = curr 
        
    mini = int(1e9)
    
    for i in range ( totalSum +1): 
        if prev[i]: 
            diff = abs(i - (totalSum - i ))
            mini = min(mini,diff)
            
    return mini
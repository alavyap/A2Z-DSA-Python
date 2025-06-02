'''

Link :> https://leetcode.com/problems/partition-equal-subset-sum/description/


Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100


'''

def canPartition(nums): 
    
    n = len(nums)
    totalSum = sum(nums)
    
    if totalSum %2 == 1 :
        return False
    else: 
        k = totalSum //2 
        dp = [[-1 for _ in range (k+1)] for _ in range (n)]
        return helper(n-1,k,nums,dp)

def helper(ind,target,nums,dp): 
    
    if target == 0: 
        return True 
    
    if ind == 0 : 
        return nums[0] == target 
    
    if dp[ind][target] != -1 : 
        return dp[ind][target]
    
    notTaken = helper(ind-1,target,nums,dp)
    
    taken = False 
    if nums[ind] <= target: 
        taken = helper(ind-1,target- nums[ind],nums,dp)        
        
    dp[ind][target] = notTaken or taken
    return dp[ind][target]


# Tabulation 
def equal(nums): 
    n = len(nums)
    totalSum = sum(nums)
    
    if totalSum % 2 == 1: 
        return False 
    
    else: 
        k = totalSum // 2 
        dp = [[False for _ in range (k +1)] for _ in range (n)]
        
        for i in range (n): 
            dp[i][0] = True 
            
        if nums[0] <= k :
            dp[0][nums[0]] = True  
            
        for ind in range (1,n): 
            for target in range (1,k +1): 
                notTaken = dp[ind -1 ][target]
                
                taken = False 
                if nums[ind] <= target: 
                    taken = dp[ind-1][target - nums[ind]]
                    
                dp[ind][target] = notTaken or taken
                
    return dp[n-1][k]
            
            
# Space Optimization 
def canPartition(nums): 
    n= len(nums)
    totSum = sum(nums)
    
    if totSum % 2 == 1 : 
        return False 
    else: 
        k = totSum // 2 
        prev = [False] * (k+1)
        prev[0] = True 
        
        if nums[0] <= k : 
            prev[nums[0]] = True
        
        for ind in range (1,n): 
            curr = [False] * (k+1)
            curr[0] = True 
            
            for target in range (1,k+1): 
                notTaken = prev[target]
                
                taken = False
                if nums[ind] <= target: 
                    taken = prev[target - nums[ind]]
                curr[target] = notTaken or taken 
            prev = curr         
    return prev[k]
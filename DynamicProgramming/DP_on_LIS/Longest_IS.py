'''
Link :> https://leetcode.com/problems/longest-increasing-subsequence/description/


Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
 
Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
 

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
'''

# Memoization >> This will return TLE 
import bisect


def longestIncreasingSubsequence(nums):
    
    n = len(nums)    
    dp = [[-1 for _ in range (n+1)] for _ in range (n)]
    return helper(nums,n,0,-1,dp)

def helper(arr,n,ind,prev_ind,dp): 
    
    if ind == n : 
        return 0 
    
    if dp[ind][prev_ind +1] != -1: 
        return dp[ind][prev_ind +1]
    
    notTake = 0 + helper(arr,n,ind+1,prev_ind,dp)
    take = 0 
    
    if prev_ind == -1 or arr[ind] > arr[prev_ind]: 
        take = 1 + helper(arr,n,ind+1,ind,dp)
        
    dp[ind][prev_ind+1] = max(notTake,take)
    return dp[ind][prev_ind +1]


# Tabulation
def tabLIS(nums): 
    n = len(nums)
    dp = [1] * n 
    
    for i in range (n): 
        for prevInd in range (i): 
            if nums[prevInd] < nums[i]: 
                if nums[prevInd] < nums[i]: 
                    dp[i] = max(dp[i] , 1 + dp[prevInd])
    return max(dp)


# Space Optimization
def spaceLIS(nums): 
    
    n = len(nums)
    nextDP = [0] * (n+1)
    
    for ind in range (n-1,-1,-1): 
        curr = [0] * (n+1)
        for prevInd in range (ind -1,-2,-1): 
            notTake = nextDP[prevInd +1]
            take = 0 
            
            if prevInd == -1 or nums[ind] > nums[prevInd]: 
                take =  1 + nextDP[ind+1]
            curr[prevInd + 1] = max(take,notTake)
        nextDP = curr 
    return nextDP[0]  

# Optimal Approach  :: O(n log(n)) time complexity
def LIS(nums): 
    
    n = len(nums)
    
    temp = [nums[0]]
    length = 1 
    
    for i in range (1,n): 
        if nums[i] > temp[-1]: 
            temp.append(nums[i])
            length += 1 
        else: 
            ind = bisect.bisect_left(temp,nums[i])
            temp[ind] = nums[i] 
            
    return length
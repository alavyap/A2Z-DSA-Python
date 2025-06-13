'''
Link :> https://leetcode.com/problems/number-of-longest-increasing-subsequence/

Given an integer array nums, return the number of longest increasing subsequences.
Notice that the sequence has to be strictly increasing.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:
Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of the longest increasing subsequence is 1, and there are 5 increasing subsequences of length 1, so output 5.
 

Constraints:

1 <= nums.length <= 2000
-106 <= nums[i] <= 106
The answer is guaranteed to fit inside a 32-bit integer.
'''
def CountLIS(nums):
    
    n = len(nums)
    dp = [1] * n 
    count = [1] * n 
    
    maxi = 1 
    
    for i in range (n): 
        for prevInd in range (i): 
            if nums[prevInd] < nums[i] and dp[prevInd] + 1 > dp[i]: 
                dp[i] = dp[prevInd]  +1
                
                count[i] = count[prevInd]
            elif nums[prevInd] < nums[i] and dp[prevInd] + 1 == dp[i]: 
                count[i] += count[prevInd]
            maxi = max(maxi,dp[i])
            
            
    numOf_LIS = 0 
    for i in range (n): 
        if dp[i] == maxi: 
            numOf_LIS += count[i] 
            
    return numOf_LIS
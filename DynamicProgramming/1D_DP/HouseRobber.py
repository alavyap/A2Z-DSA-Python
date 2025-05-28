'''

Link :> https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
'''

# Memoization  
def main(nums):
    n = len(nums)
    dp = [-1] * n
    return helper(n-1,nums,dp)

def helper(index,nums,dp): 
    if index == 0 : 
        return nums[index]
    if dp[index] != -1 :
        return dp[index]
    if index < 0 :
        return 0
    
    notPick = 0 + helper(index-1,nums,dp)
    pick = helper(index-2,nums,dp) + (nums[index])
    dp[index] = max(notPick,pick)
    return dp[index]


# Tabulation 
def robber(nums):
    n = len(nums)
    dp = [-1] * n
    dp[0] = nums[0]
    for index in range (1,n): 
        notPick = 0 +  dp[index-1]
        pick = nums[index]
        if index > 1 :
            pick += dp[index-2] 
        dp[index] = max(notPick,pick)
    return (dp[n-1])


# Space Optimization 
def house(nums): 
    n = len(nums)
    prev = nums[0]
    prev2 = 0
    
    for index in range (1,n):
        notPick =  0 + prev 
        pick = nums[index] 
        if index > 1 :
            pick += prev2 
        curr = max(notPick,pick)
        prev2 = prev 
        prev = curr 
    return (prev)
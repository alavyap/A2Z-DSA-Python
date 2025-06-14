'''
Link :> https://leetcode.com/problems/burst-balloons/description/

You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
Example 2:

Input: nums = [1,5]
Output: 10
 

Constraints:
n == nums.length
1 <= n <= 300
0 <= nums[i] <= 100
'''

# Memoization 
def maxCoins(nums):
    
    n = len(nums)
    nums.insert(0,1)
    nums.append(1)
    
    dp = [[-1] * (n +2) for _ in range (n +2)]
    
    def helper(i,j):
        if i > j : 
            return 0 
        
        if dp[i][j] != -1 : 
            return dp[i][j] 
        maxi = float("-inf")
        for ind in range(i,j+1): 
            cost = nums[i-1] * nums[ind] * nums[j+1] + helper(i,ind -1) + helper(ind +1,j)
            maxi = max(maxi,cost)
        dp[i][j] = maxi 
        return maxi  
    
    return helper(1,n)


# Tabulation 
def coinsMax(nums):
    
    n = len(nums)
    nums.insert(0,1)
    nums.append(1)
    
    dp = [[0] * (n +2) for _ in range (n +2)]
    
    for i in range (n,0,-1): 
        for j in range (1,n +1): 
            if i > j : 
                continue
            maxi = float("-inf")
            
            for ind  in range (i,j+1):
                cost = nums[i-1] * nums[ind] * nums[j+1] + dp[i][ind-1] + dp[ind+1][j] 
                maxi = max(maxi,cost)
            dp[i][j] = maxi 
            
    return dp[1][n] 
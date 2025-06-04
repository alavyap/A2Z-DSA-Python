'''
link :> https://leetcode.com/problems/coin-change-ii/description/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

 

Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1
 

Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000


'''

# Memoization
def coinChange(amount,coins):
    n = len(coins)
    dp = [[-1 for _ in range (amount+1)] for _ in range (n)]
    return helper(coins,n-1,amount,dp)

def helper(arr,ind,total,dp): 
    
    if ind == 0 : 
        return 1 if total % arr[0] == 0 else 0 
    
    if dp[ind][total] != -1 : 
        return dp[ind][total]
    
    notTaken = helper(arr,ind -1,total, dp)
    taken = 0 
    if arr[ind] <= total: 
        taken = helper(arr,ind,total- arr[ind],dp)
    
    dp[ind][total] = notTaken + taken 
    return dp[ind][total]


# Tabulation 
def countChange(amount,coins): 
    n = len(coins)
    dp = [[0 for _ in range (amount + 1)] for _ in range (n)]
    
    for i in range (amount +1): 
        if i % coins[0] == 0 :
            dp[0][i] = 1 
            
    for ind in range (1,n): 
        for target in range (amount+1): 
            notTaken = dp[ind - 1][target]
            
            taken = 0 
            if coins[ind] <= target: 
                taken = dp[ind][target - coins[ind]]
            dp[ind][target] = notTaken + taken 
            
    return dp[n-1][amount]

# Space Optimization 
def getTarget(amount,coins): 
    n = len(coins)
    prev = [0] * (amount +1)
    
    for i in range (amount + 1 ): 
        if i % coins[0] == 0: 
            prev[i] = 1 
    
    for ind in range (1,n): 
        curr = [0] * (amount+1)
        for target in range (amount +1): 
            notTaken = prev[amount]
            
            taken = 0 
            if coins[ind] <= amount :
                taken = curr[target - coins[ind]]
                
            curr[amount] = notTaken + taken 
            
        prev = curr 
    return prev[amount] 
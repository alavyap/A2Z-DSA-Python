'''
Link :> https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


'''
# Memoization 
def coinChange(coins,amount): 
    n = len(coins)
    dp = [[-1 for _ in range  (amount + 1)] for _ in range (n)]
    ans = helper(coins,n-1,amount,dp)
    
    if ans >= int(1e9):
        return -1
    return ans 

def helper(arr,ind,T,dp):
    
    if ind ==0 : 
        if T % arr[0] == 0 : 
            return T // arr[0] 
        else: 
            return int(1e9)
    
    if dp[ind][T] != -1 : 
        return dp[ind][T]
    
    notTaken =  0 + helper(arr,ind -1,T,dp)
    taken = int(1e9)
    
    if arr[ind] <= T :
        taken = 1 + helper(arr,ind,T - arr[ind],dp)
        
    dp[ind][T] = min(notTaken,taken)
    return dp[ind][T]
    

# Tabulation 
def changes(coins,amount): 
    
    n = len(coins)
    dp = [[0 for _ in range (amount +1)] for _ in range (n)]
    
    for i  in range (amount +1 ):
        if i % coins[0] == 0 : 
            dp[0][i] = i // coins[0] 
        else :
            dp[0][i] = int(1e9)
            
    for ind in range (1,n): 
        for target in range (amount +1) : 
            notTaken = dp[ind-1][target]
            taken = int(1e9)
            if coins[ind] <= target: 
                taken = 1 + dp[ind][target - coins[ind]] 
            dp[ind][target] = min(notTaken,taken) 
    ans = dp[n-1][amount]
    
    if ans >= int(1e9): 
        return -1 
    return ans 

# Space Optimization 
def minCoin(coins,amount): 
    n = len(coins)
    
    prev = [0] * (amount + 1)
    curr = [0] * (amount + 1)
    
    for i in range (0,1+amount): 
        if i % coins[0] == 0 : 
            prev[i]  = i // coins[0]
        else: 
            prev[i] = int(1e9)
            
    for ind in range (1,n): 
        for target in range (amount + 1): 
            notTake = prev[target]
            take = int(1e9)
            
            if coins[ind] <= target: 
                take = 1 + curr[target - coins[ind]]
            curr[target] = min(notTake,take)
        prev = curr 
        
    ans = prev[amount]
    
    if ans >= int(1e9) :
        return -1 
    return ans  
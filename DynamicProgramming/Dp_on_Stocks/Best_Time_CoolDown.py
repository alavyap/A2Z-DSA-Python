'''
Link :> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000

'''

# Memoization
def coolDown(prices): 
    n = len(prices)
    dp = [[-1 for _ in range (2)] for _ in range (n)]
    
    return helper(prices,0,0,n,dp)


def helper(prices,ind,buy,n,dp): 
    
    if ind >= n : 
        return 0 
    
    if dp[ind][buy] != -1: 
        return dp[ind][buy]
    
    profit = 0 
    
    if buy == 0 : 
        profit = max(
            0 +helper(prices,ind+1,0,n,dp),
            -prices[ind] + helper(prices,ind+1,1,n,dp)
        )
        
    else : 
        profit = max(
            0 + helper(prices,ind+1,1,n,dp),
            prices[ind] + helper(prices,ind+2,0,n,dp)
        )
        
    dp[ind][buy] = profit 
    return profit

# Tabulation 
def stockCoolDown(prices): 
    n = len(prices)
    dp = [[0 for _ in range (2)] for _ in range (n +2)]
    
    for ind in range (n-1,-1,-1): 
        for buy in range (2): 
            profit = 0 
            
            if buy == 0 : 
                profit = max(0 + dp[ind+1][0], -prices[ind] + dp[ind+1][1])
                
            else: 
                profit = max( 0 + dp[ind+1][1], prices[ind] + dp[ind+2][0])
                
            dp[ind][buy] = profit 
            
    return dp[0][0]


# Space Optimization 
def marketCoolDown(prices): 

    n = len(prices)
    curr = [0,0]
    front1 = [0,0] 
    front2 = [0,0] 
    
    for ind in range (n-1,-1,-1): 
        for buy in range (2): 
            profit = 0 
            
            if buy == 0 : 
                profit = max(
                    0 + front1[0], -prices[ind] + front1[1]
                )                
            else: 
                profit = max(0 + front1[1], prices[ind] + front2[0])
            curr[buy] = profit 
            
        front2 = front1.copy()
        front1 = curr.copy() 
    return curr[0]
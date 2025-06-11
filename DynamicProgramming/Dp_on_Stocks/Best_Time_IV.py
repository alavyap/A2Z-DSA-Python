'''
Link :> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
 

Constraints:

1 <= k <= 100
1 <= prices.length <= 1000
0 <= prices[i] <= 1000
'''

# Memoization 
def maxProfit(k,prices): 
    n = len(prices)
    dp = [[[(-1) for _ in range (k +1)] for _ in range (2)] for _ in range (n)]
    return helper(prices,n,0,0,k,dp)

def helper(prices,n,ind,buy,cap,dp): 
    
    if ind == n or cap == 0: 
        return 0 
    
    if dp[ind][buy][cap] != -1: 
        return dp[ind][buy][cap]
    
    profit = 0 
    
    if buy == 0 : 
        profit = max(
            0 + helper(prices,n,ind+1,0,cap,dp), -prices[ind] + helper(prices,n, ind +1,1,cap,dp))
    
    else :
        profit = max(
            0 + helper(prices,n,ind+1,1,cap,dp), prices[ind] + helper(prices,n,ind+1,0,cap -1,dp)
        )
        
    dp[ind][buy][cap] = profit
    return profit


# Tabulation 
def maximum_profit(k,prices): 
   
    n = len(prices)    
    dp = [[[0 for _ in range (k +1)]for _ in range (2)] for _ in range (n+1)]
    
    for ind in range (n-1,-1,-1): 
        for buy in range (2): 
            for cap in range (1, k +1): 
                
                if buy == 0 : 
                    dp[ind][buy][cap] = max(0 + dp[ind+1][0][cap], -prices[ind] + dp[ind+1][1][cap])
                else: 
                    dp[ind][buy][cap] = max(0 + dp[ind+1][1][cap], prices[ind] + dp[ind +1][0][cap -1])
                    
    return dp[0][0][k] 

# Space Optimization 

def maxProfit(k,prices): 
    n = len(prices)
    
    ahead = [[0] * (k +1) for _ in range (2)]
    curr = [[0] * (k +1) for _ in range (2)]
    
    for ind in range (n-1,-1,-1): 
        for buy in range (2): 
            for cap in range (1,k+1): 
                
                if buy == 0 : 
                    curr[buy][cap] = max(0 + ahead [0][cap], -prices[ind] + ahead[1][cap])
                else:
                    curr[buy][cap] = max(0 + ahead[1][cap],prices[ind] + ahead[0][cap-1])
                    
        ahead = curr.copy() 
    return ahead[0][k]
'''
Link :> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again). 

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
'''

# Memoization 
def maxProfit(prices): 
    
    n = len(prices)
    dp = [[[-1 for _ in range (3)] for _ in range (2)] for _ in range (n)]
    
    def helper(ind,buy,cap): 
        
        if ind == n or cap == 0: 
            return 0 
        
        if dp[ind][buy][cap] != -1: 
            return dp[ind][buy][cap]
        
        profit = 0 
        
        if buy == 0 : 
            profit = max(0 + helper(ind+1,0,cap),-prices[ind] + helper(ind+1,1,cap))
        else : 
            profit = max(0 + helper(ind +1,1,cap), prices[ind]+helper(ind +1,0,cap -1))
            
        dp[ind][buy][cap] = profit 
        return profit 
    return helper(0,0,2)


# Tabulation 
def profitMax(prices): 
    
    n = len(prices)
    dp = [[[0 for _ in range (3)] for _ in range (2)] for _ in range (n + 1)]
    
    for ind in range (n-1,-1,-1): 
        for buy in range (2): 
            for cap in range (1,3): 
                
                if buy == 0 : 
                    dp[ind][buy][cap] = max(0  + dp[ind+1][0][cap], -prices[ind] + dp[ind+1][1][cap])
                else: 
                    dp[ind][buy][cap] = max(0 + dp[ind+1][1][cap],prices[ind] + dp[ind][0][cap-1])
                    
    return dp[0][0][2]


# Space Optimization 
def buySell_III(prices): 
    n = len(prices)
    
    ahead = [[0 for _ in range (3)]for _ in range (2)]
    curr = [[0 for _ in range (3)]for _ in range (2)]
    
    for ind in range (n-1,-1,-1): 
        for buy in range (2): 
            for cap in range (1,3): 
                
                if buy == 0 : 
                    curr[buy][cap] = max(0+ ahead[0][cap], -prices[ind] + ahead[1][cap])
                else: 
                    curr[buy][cap] = max(0 + ahead[1][cap], prices[ind] + ahead[0][cap-1])

            ahead = curr 
    return ahead[0][2]                    
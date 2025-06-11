'''
Link :> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.
Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note:

You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
The transaction fee is only charged once for each stock purchase and sale.
 

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6
 
Constraints:

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
'''
# Memoization
def Fees(prices,fee):
    n = len(prices)
    
    dp = [[-1 for _ in range (2)] for _ in range (n)]
    if n == 0 : return 0 
    
    return helper(prices,0,0,n,fee,dp)

def helper(prices,ind,buy,n,fee,dp): 
    
    if ind == n : 
        return 0 

    if dp[ind][buy] != -1: 
        return dp[ind][buy]
    
    profit = 0 
    
    if buy == 0 : 
        profit = max(0 + helper(prices,ind +1,0,n,fee,dp), -prices[ind] + helper(prices,ind+1,1,n,fee,dp))
        
    else: 
        profit = max(0 + helper(prices,ind+1,1,n,fee,dp), prices[ind] - fee + helper(prices,ind+1,0,n,fee,dp))
        
    dp[ind][buy] = profit
    return profit

# Tabulation
def TotalTransactions(prices,fee):
    n = len(prices)
    
    dp = [[0 for _ in range (2)] for _ in range (n +1)]
    
    for ind in range (n-1,-1,-1): 
        for buy in range (2): 
            profit = 0 
            
            if buy == 0 : 
                profit = max(0 + dp[ind+1][0], -prices[ind] + dp[ind+1][1])
            else: 
                profit = max(0 + dp[ind+1][1], prices[ind] - fee + dp[ind+1][0])
            
            dp[ind][buy] = profit
    return dp[0][0]

# Space Optimization 
def optimalApproach(prices,fee): 
    
    n = len(prices)
    
    if n == 0: 
        return 0 
    
    ahead = [0,0] 
    curr = [0,0]
    
    ahead[0] = ahead[1] = 0 
    
    for ind in range (n-1,-1,-1): 
        for buy in range (2): 
            profit = 0 
            
            if buy == 0: 
                profit = max(0 + ahead[0] , -prices[ind] + ahead[1])
                
            else: 
                profit = max(0 + ahead[1], prices[ind]-fee + ahead[0])
                
            curr[buy] = profit 
            
        ahead = curr.copy() 
    return curr[0] 
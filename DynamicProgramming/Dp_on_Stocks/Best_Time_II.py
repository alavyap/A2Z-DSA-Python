'''
Link :> https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104


'''

# Memoization 
def buySell(prices): 
    n = len(prices)
    maxProfit = helper(prices,n)
    return maxProfit


def helper(prices,n): 
    
    if n == 0: 
        return 0 
    dp = [[-1 for _ in range (2)] for _ in range (n)]
    
    def getAns(ind,buy): 
        if ind == n :
            return 0 
        
        if dp[ind][buy] != -1:
            return dp[ind][buy]
        if buy == 0 : 
            profit = max(0 + getAns(ind+1,0), -prices[ind] + getAns(ind +1,1))
        elif buy == 1 : 
            profit  = max(0 + getAns(ind+1,1), prices[ind] + getAns(ind+1,0))
        
        dp[ind][buy] = profit
        return profit
    ans = getAns(0,0)
    return ans 


# Tabulization 
def getMaxProfit(prices): 
    
    n = len(prices)
    dp = [[-1 for _ in range (2)] for _ in range (n+1)]
    dp[n][0] = dp[n][1] = 0 
    
    for ind in range (n-1,-1,-1): 
        for buy in range (2): 
            profit = 0 
            
            if buy == 0 : 
                profit = max(0 + dp[ind +1][0], -prices[ind]+ dp[ind + 1][1])
            elif buy == 1: 
                profit = max(0 + dp[ind +1][1], prices[ind] + dp[ind+1][0])
            dp[ind][buy] = profit 
    return dp[0][0]


# Space Optimization 

def getMaximum(prices):
    n = len(prices)
    
    ahead = [0,0]
    curr = [0,0] 
    
    ahead[0] = ahead[1] = 0 
    
    for ind in range (n-1,-1,-1): 
        for buy in range (2): 
            profit = 0 
            
            if buy == 0: 
                profit = max(0 + ahead[0], -prices[ind] + ahead[1])
            elif buy == 1 : 
                profit = max(0 + ahead[1], prices[ind] + ahead[0])
            curr[buy] = profit 
            
        ahead = curr 
    return curr[0]
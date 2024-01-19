'''
Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. 
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and 
sell on day 5 (price = 6), profit = 6-1 = 5.
'''
# Brute Force




import profile


def CNstock (prices):
    n = len(prices)
    profit = 0
    '''
    My Logic
    buy = float('inf')
    sell = float('-inf') 
    
    for i in range (n):
        if prices[i] < buy :
            buy = prices[i]
            
        for j in range (prices[i]+1,n):
            if prices[j] > sell :
                sell = prices[j] 
        profit = sell - buy
        if (profit) > 0 :
            return (profit)
    return 0
    
    '''
    for i in range (n):
        for j in range (i+1,n):
            if prices[j] > prices[i] :
                if profit < (prices[j]- prices[i]):
                    profit = prices[j] - prices[i]
    return profit

# Test Run 
# print (CNstock ([7,1,5,3,6,4]))


# Optimal Approach 
def stocks(prices):
    n = len(prices)
    profit = 0
    buy = float('inf')
    for i in range (n):
        if prices[i] < buy :
            buy = prices[i]
        if profit < (prices[i] - buy):
            profit = prices[i] - buy
            
    return profit
    
# Test Run   
print (stocks([7,1,5,3,6,4]))
'''
Link :> https://www.naukri.com/code360/problems/unbounded-knapsack_1215029?source=youtube&campaign=striver_dp_videos

You are given ‘n’ items with certain ‘profit’ and ‘weight’ and a knapsack with weight capacity ‘w’.
You need to fill the knapsack with the items in such a way that you get the maximum profit. You are allowed to take one item multiple times.

Example:
Input: 
'n' = 3, 'w' = 10, 
'profit' = [5, 11, 13]
'weight' = [2, 4, 6]

Output: 27

Explanation:
We can fill the knapsack as:

1 item of weight 6 and 1 item of weight 4.
1 item of weight 6 and 2 items of weight 2.
2 items of weight 4 and 1 item of weight 2.
5 items of weight 2.

The maximum profit will be from case 3 = 11 + 11 + 5 = 27. Therefore maximum profit = 27.


Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
3 15
7 2 4
5 10 20


Expected Answer:
21
Output on console:
21


Explanation of Sample Input 1
The given knapsack capacity is 15. We can fill the knapsack as [1, 1, 1] giving us profit 21 and as [1,2] giving us profit 9. Thus maximum profit will be 21.


Sample Input 2
2 3
6 12
4 17
Expected Answer:
0
Output on console:
0

Explanation of Sample Input 2:
We can clearly see that no item has weight less than knapsack capacity. Therefore we can not fill knapsack with any item.


Expected Time Complexity:
Try to solve this in O(n*w).


Constraints
1 <= n <= 10^3
1 <= w <= 10^3
1 <= profit[i] , weight[i] <= 10^8

Time Limit: 1 sec
'''

import sys

# Memoization 
def unboundedKnapsack(n,w,profit,weight):
    
    dp = [[-1 for _ in range(w+1)] for _ in range (n)]
    return helper(weight,profit,n-1,w,dp)

def helper(wt,val,ind,w,dp):
    
    if ind ==0 : 
        return (w //wt[0]) * val[0]
    
    if dp[ind][w] != -1 :
        return dp[ind][w]
    
    notTaken = helper(wt,val,ind -1,w,dp)
    
    taken = -sys.maxsize
    if wt[ind] <= w: 
        taken = val[ind] +helper(wt,val,ind,w-wt[ind],dp)
    dp[ind][w] = max(notTaken,taken)
    return dp[ind][w]


# Tabulation
def unKnapsack(n,w,profit,weight):
    dp = [[0 for _ in range (w+1)] for _ in range (n)]
    
    for i in range (weight[0],w+1,weight[0]):
        dp[0][i] = ((i //weight[0] * profit[0]))
        
    for ind in range (1,n): 
        for cap in range (w +1): 
            notTaken = 0 + dp[ind -1][cap]
            
            taken = -sys.maxsize
            if weight[ind] <= cap: 
                taken = profit[ind] + dp[ind][cap - weight[ind]]
            dp[ind][cap] = max(notTaken,taken)
        
    return dp[n-1][w]


def knapsack(n,w,profit,weight): 
    
    curr = [0] * (w +1)
    
    for i in range (weight[0], w+1): 
        curr[i] = ( i // weight[0])  * profit[0]
        
    for ind in range (1,n): 
        for cap in range (w +1): 
            notTaken = curr[cap]
            
            taken = - sys.maxsize
            if weight[ind] <= cap: 
                taken  = profit[ind] + curr[cap - weight[ind]]
                
            curr[cap] = max(notTaken,taken)
            
    return curr[w]
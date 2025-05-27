'''
Link :> https://www.geeksforgeeks.org/problems/geek-jump/1

Given an integer array height[] where height[i] represents the height of the i-th stair, a frog starts from the first stair and wants to reach the top. From any stair i, the frog has two options: it can either jump to the (i+1)th stair or the (i+2)th stair. The cost of a jump is the absolute difference in height between the two stairs. Determine the minimum total cost required for the frog to reach the top.

Example:

Input: heights[] = [20, 30, 40, 20] 
Output: 20
Explanation:  Minimum cost is incurred when the frog jumps from stair 0 to 1 then 1 to 3:
jump from stair 0 to 1: cost = |30 - 20| = 10
jump from stair 1 to 3: cost = |20-30|  = 10
Total Cost = 10 + 10 = 20
Input: heights[] = [30, 20, 50, 10, 40]
Output: 30
Explanation: Minimum cost will be incurred when frog jumps from stair 0 to 2 then 2 to 4:
jump from stair 0 to 2: cost = |50 - 30| = 20
jump from stair 2 to 4: cost = |40-50|  = 10
Total Cost = 20 + 10 = 30
Constraints:

1 <= height.size() <= 105
0 <= height[i]<=104

'''
# Recursion 
def recursion(height):
   n = len(height)   
   return helper(n-1,height)

def helper(i,heights): 
    if i == 0 :
        return 0     
    cost1 = helper(i-1,heights) + abs(heights[i] - heights[i-1])
    cost2 = float("inf")
    if i > 1 : 
        cost2 = helper(i-2,heights) + abs(heights[i] - heights[i-2])
    return min(cost1,cost2 )  


# Memoization 
def mainF(height):
    n = len(height)
    dp = [-1] * n+1
    return (helper(n-1, height,dp))

def helper (index,height,dp):
     
    if index == 0 : 
        return 0 
    if dp[index] != -1 : 
        return dp[index]
    cost1 = helper(index-1,height,dp) + abs(height[index] - height[index-1])
    cost2 = float("inf")
    
    if index > 1 :
        cost2 = helper(index-2,height,dp) + abs(height[index] - height[index-2])
    dp[index] = min(cost1,cost2)
    return dp[index] 

#Tabulation

def  frog(height): 
    n = len(height)
    dp = [-1] * n 
    dp[0] = 0
    for index in range (1,n): 
        cost1 = dp[index-1] + abs(height[index]- height[index-1])
        cost2 = float("inf")
        if index > 1 : 
            cost2 = dp[index -2 ] + abs(height[index] - height[index-2])
        dp[index] = min(cost1,cost2)
    return( dp[n-1])


# Space Optimization
def spaceFrog(height):
    n = len(height)
    prev = 0
    prev2 = 0
    
    for i in range (1,n): 
        cost1  = prev + abs(height[i] - height[i-1])
        cost2 = float("inf")
        if i > 1 :
           cost2 = prev2 + abs(height[i] - height[i-2])
        curr = min(cost1,cost2)
        prev2 = prev 
        prev = curr
    return (prev)
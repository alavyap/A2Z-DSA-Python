'''
Link :> https://takeuforward.org/data-structure/subset-sum-equal-to-target-dp-14/

You are given an array/list ‘ARR’ of ‘N’ positive integers and an integer ‘K’. Your task is to check if there exists a subset in ‘ARR’ with a sum equal to ‘K’.

Note: Return true if there exists a subset with sum equal to ‘K’. Otherwise, return false.

For Example :
If ‘ARR’ is {1,2,3,4} and ‘K’ = 4, then there exists 2 subsets with sum = 4. These are {1,3} and {4}. Hence, return true.
Detailed explanation ( Input/output format, Notes, Images )
Constraints:
1 <= T <= 5
1 <= N <= 10^3
0 <= ARR[i] <= 10^9
0 <= K <= 10^3

Time Limit: 1 sec
Sample Input 1:
2
4 5
4 3 2 1
5 4
2 5 1 6 7
Sample Output 1:
true
false
Explanation For Sample Input 1:
In example 1, ‘ARR’ is {4,3,2,1} and ‘K’ = 5. There exist 2 subsets with sum = 5. These are {4,1} and {3,2}. Hence, return true.
In example 2, ‘ARR’ is {2,5,1,6,7} and ‘K’ = 4. There are no subsets with sum = 4. Hence, return false.
Sample Input 2:
2
4 4
6 1 2 1
5 6
1 7 2 9 10
Sample Output 2:
true
false
Explanation For Sample Input 2:
In example 1, ‘ARR’ is {6,1,2,1} and ‘K’ = 4. There exist 1 subset with sum = 4. That is {1,2,1}. Hence, return true.
In example 2, ‘ARR’ is {1,7,2,9,10} and ‘K’ = 6. There are no subsets with sum = 6. Hence, return false.


Hints:
1. Can you find every possible subset of ‘ARR’ and check if its sum is equal to ‘K’?
2. Can you use dynamic programming and use the previously calculated result to calculate the new result?
3. Try to use a recursive approach followed by memoization by including both index and sum we can form. 

'''

def subSet(n,k, arr): 
    
    
    dp = [[-1 for _ in range (k+1)] for _ in range (n)]
    
    return helper(n-1,k,arr,dp)


def helper(index,target,arr,dp): 
    if target == 0 :
        return True 
    
    if index == 0:
        return arr[0] == target 
    
    if dp[index][target] != -1: 
        return dp[index][target]
    
    notTaken = helper(index-1,target,arr,dp)
    
    taken = False 
    
    if arr[index] <= target: 
        taken = helper(index - 1, target- arr[index],arr,dp)
    
    dp[index][target] = notTaken or taken 
    return dp[index][target]

         
# Tabulation
def subSet(n,k,arr): 
    
    dp = [[False for _ in range (k+1)] for _ in range (n)]
    
    for i in range (n): 
        dp[i][0] = True 
        
    if arr[0] <= k : 
        dp[0][arr[0]] = True 
        
    for index in range (1,n): 
        for target in range (1,k+1): 
            notTaken = dp[index - 1 ][target]
            taken = False 
            
            if arr[index] <= target: 
                taken = dp[index - 1][target - arr[index]]
            dp[index][target] = notTaken or taken      
    return dp[n-1][k]

# Space Optimization 
def subSet(n,k,arr): 
    prev = [False]  * (k +1)
    prev[0] = True 
    
    if arr[0] <= k : 
        prev[arr[0]] = True 
        
    for index in range (1,n): 
        curr = [False] * (k+1)
        curr[0] = True 
        
        for target in range (1,k+1): 
            not_taken = prev[target]
            taken = False 
            
            if arr[index] <= target: 
                taken = prev[target - arr[index]]
                
            curr[target] = not_taken or taken 
        prev = curr 
        
    return prev[k] 
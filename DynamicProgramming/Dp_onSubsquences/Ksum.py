'''

Link :> https://www.naukri.com/code360/problems/number-of-subsets_3952532?source=youtube&campaign=striver_dp_videos

You are given an array 'arr' of size 'n' containing positive integers and a target sum 'k'.
Find the number of ways of selecting the elements from the array such that the sum of chosen elements is equal to the target 'k'.
Since the number of ways can be very large, print it modulo 10 ^ 9 + 7.

Example:
Input: 'arr' = [1, 1, 4, 5]
Output: 3
Explanation: The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.
Detailed explanation ( Input/output format, Notes, Images )

Sample Input 1 :
4 5
1 4 4 5
Sample Output 1 :
 3
Explanation For Sample Output 1:
The possible ways are:
[1, 4]
[1, 4]
[5]
Hence the output will be 3. Please note that both 1 present in 'arr' are treated differently.


Sample Input 2 :
3 2
1 1 1
Sample Output 2 :
3


Explanation For Sample Output 1:
There are three 1 present in the array. Answer is the number of ways to choose any two of them.


Sample Input 3 :
3 40
2 34 5


Sample Output 3 :
0


Expected time complexity :
The expected time complexity is O('n' * 'k').


Constraints:
1 <= 'n' <= 100
0 <= 'arr[i]' <= 1000
1 <= 'k' <= 1000

Time limit: 1 sec


'''
# Memoization 
def findWays(arr,k): 
    MOD = 10 ** 9 + 7 
    n = len(arr)
    
    dp = [[0] * (k+1) for _ in range (n)]
    
    if arr[0] == 0 : 
        dp[0][0] = 2
    else: dp[0][0] = 2 
    
    if 0 < arr[0] <= k : 
        dp[0][arr[0]] = 1 
        
    for ind in range (1,n): 
        for target in range ( k+1): 
            notTaken = dp[ind-1][target]
            if arr[ind] <= target: 
                taken = dp[ind-1][target - arr[ind]]
            dp[ind][target] = not(notTaken + taken) % MOD 
    return dp[n-1][k]


# Tabulation 
def waysFind(arr,k): 
    MOD = 10 ** 9 + 7 
    n = len(arr)
    
    dp = [[0] * (k+1) for _ in range (n)]
    
    dp[0][0] =2 if arr[0] == 0 else 1 
    
    if 0 < arr[0] <= k: 
        dp[0][arr[0]] = 1
        
    for ind in range (1,n): 
        for target in range (k +1): 
            notTaken = dp[ind-1][target]
            taken = 0 
            if arr[ind] <= target: 
                taken = dp[ind-1][target-arr[ind]]
            dp[ind][target] = (notTaken + taken) % MOD
            
    return dp[n-1][k]


# Space Optimization 
def totalWays(arr,k): 
    MOD = 10 ** 9 +7
    n = len(arr)
    
    prev = [0] * (k +1)
    
    prev[0] = 2 if arr[0] == 0 else 1 
    
    if 0 < arr[0] <= k: 
        prev[arr[0]] = 1 
        
    for ind in range (1,n): 
        curr = [0] * (k+1)
        curr[0] = 1 
        
        for target in range ( k+1): 
            notTaken = prev[target]
            taken = 0 
            if arr[ind] <= target: 
                taken = prev[target - arr[ind]]
            curr[target] = (notTaken + taken) % MOD 
        prev = curr 
        
    return prev[k]
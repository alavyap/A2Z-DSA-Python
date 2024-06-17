'''
GFG :> https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/

Given an array arr of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.
Note: Answer can be very large, so, output answer modulo 10 ** 9+7.

Example :
Input: 
N = 6
arr = [5, 2, 3, 10, 6, 8]
sum = 10
Output: 
3
Explanation: 
{5, 2, 3}, {2, 8}, {10} are possible subsets.

'''

# Recursive Approach
def perfectSum(arr, n, sum):
		# code here
		# Initialize a dynamic programing array with 0 based indexing 
    
        dp = [1] +[0] * sum  #dp[i] represents the count of perfect sums that add up to 'i' 
        
        MOD = 10 ** 9 + 7
       # Iterate through the possible sums in reverse order 
        
        for number in arr :    
        
            for needed_sum in range (sum, number - 1, -1):
        
                dp[needed_sum] = (dp[needed_sum] + dp[needed_sum-number]) % MOD 
    
        return dp[sum]
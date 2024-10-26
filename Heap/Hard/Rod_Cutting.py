'''

LeetCode :> https://www.geeksforgeeks.org/problems/rod-cutting0840/1

Given a rod of length N inches and an array of prices, price[]. price[i] denotes the value of a piece of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Note: Consider 1-based indexing.

Example:

Input: n = 8, price[] = {1, 5, 8, 9, 10, 17, 17, 20}
Output: 22
Explanation: The maximum obtainable value is 22 by cutting in two pieces of lengths 2 and 6, i.e., 5+17=22.
Input: n = 8, price[] = {3, 5, 8, 9, 10, 17, 17, 20}
Output: 24
Explanation: The maximum obtainable value is 24 by cutting the rod into 8 pieces of length 1, i.e, 8*price[1]= 8*3 = 24.
Your Task:  You don't need to read input or print anything. Your task is to complete the function cutRod() which takes the array A[] and its size N as inputs and returns the maximum price obtainable.

Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ n≤ 1000
1 ≤ price[i] ≤ 105

'''

# This is a Dynamic Programming Question

def cutting(n,price): 
    dp = [0] * (n +1)
    for i  in range (1 , n +1):
        max_value = float('-inf')
        for j in range (i) :
            max_value = max(max_value,price[j] + dp[i-j-1])
            
        dp[i] = max_value
        
    return dp[n]

   
# Test 
price = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
print(cutting(n,price))
'''
GFG :> https://www.geeksforgeeks.org/problems/number-of-coins1824/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card

Given an array coins[] represent the coins of different denominations and a target value sum. You have an infinite supply of each of the valued coins{coins1, coins2, ..., coinsm}.  Find the minimum number of coins to make the change. If not possible to make a change then return -1.

Examples:

Input: coins[] = [25, 10, 5], sum = 30
Output: 2
Explanation: Minimum 2 coins needed, 25 and 5  
Input: coins[] = [9, 6, 5, 1], sum = 19
Output: 3
Explanation: 19 = 9 + 9 + 1
Input: coins[] = [5, 1], sum = 0
Output: 0
Explanation: For 0 sum, we do not need a coin
Input: coins[] = [4, 6, 2], sum = 5
Output: -1
Explanation: Not possible to make the given sum.
Expected Time Complexity: O(n*sum)
Expected Auxiliary Space: O(sum)
 
Constraints:
1 ≤ sum*coins.size() ≤ 106
All array elements are distinct

'''


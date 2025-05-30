'''

Link :> https://leetcode.com/problems/house-robber-ii/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000

'''
# Space Optimization 
def main (nums):
    n = len(nums)
    return robStreet(n,nums)

def robStreet(n,nums):
    arr1 = [] 
    arr2 = []    
    if n == 1 :
        return nums[0] 
    for i in range (n):
        if i != 0 :
            arr1.append(nums[i])
        if i != n-1 : 
            arr2.append(nums[i])
    ans1 = helper(arr1)
    ans2 = helper(arr2)
    return max(ans1,ans2)

def helper(nums):
    n = len(nums)
    prev = nums[0] 
    prev2 = 0 
    for i in range (1,n): 
        pick = nums[i]
        if i > 1 : 
            pick += prev2 
        notPick = 0 + prev 
        curr = max(pick,notPick)
        prev2 = prev 
        prev = curr 
    return prev 

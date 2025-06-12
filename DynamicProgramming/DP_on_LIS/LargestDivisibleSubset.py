'''
Link :> https://leetcode.com/problems/largest-divisible-subset/description/


Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
Example 2:

Input: nums = [1,2,4,8]
Output: [1,2,4,8]
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 2 * 109
All the integers in nums are unique.
'''

def longestDivSubset(nums): 
    n = len(nums)
    nums.sort()
    
    dp = [1] * n 
    hashArr = list(range(n))
    
    for i in range (n):
        for prevInd  in range (i): 
            if nums[i] % nums[prevInd] == 0 and 1 + dp[prevInd] > dp[i]: 
                dp[i]  = 1 + dp[prevInd]
                hashArr[i] = prevInd
                
    ans = -1
    lastInd = -1
    
    for i in range (n): 
        if dp[i] > ans: 
            ans = dp[i] 
            lastInd = i 
            
    result = [nums[lastInd]]
    
    while hashArr[lastInd] != lastInd: 
        lastInd = hashArr[lastInd]
        result.append(nums[lastInd])
        
    return result
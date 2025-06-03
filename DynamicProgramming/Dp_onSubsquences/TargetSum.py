'''

Link :> https://leetcode.com/problems/target-sum/description/

You are given an integer array nums and an integer target.
You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.


Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1
 
Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''

# Memoization 
from annotated_types import T


def findTarget(nums,target): 
    n = len(nums)
    totalSum = 0 
    
    for i in range (n): 
        totalSum += nums[i] 
        
    if totalSum - target < 0 : 
        return 0 
    if (totalSum - target) % 2 == 1 : 
        return 0 
    s2 = (totalSum -target) // 2 
    dp = [[-1 for _ in range (s2 +1)] for _ in range (n)]
    return helper(n-1,s2,nums,dp)


def helper(ind,target,arr,dp): 
    if ind == 0 : 
        if target == 0 and arr[0] == 0 : 
            return 2 
        if target ==0 or target == arr[0]: 
            return 1 
        return 0 
    
    if dp[ind][target] != -1 : 
        return dp[ind][target]
    
    notTaken = helper(ind -1, target,arr,dp)
    taken =  0 
    if arr[ind] <= target:
        taken = helper(ind -1,target- arr[ind],arr,dp)
    dp[ind][target] = notTaken + taken 
    return dp [ind][target]



# Tabulation 
MOD = int(1e9+7)
def sumTarget( nums,target): 

    totalSum = 0 
    for i in range (len(nums)): 
        totalSum += nums[i] 
        
    if (totalSum - target) < 0 or ((totalSum - target) % 2 ):
        return  0 
    return helper(nums,(totalSum - target) // 2)


def helper(nums,tar): 
    n = len(nums)
    dp = [[0 for _ in range (tar +1 )] for _ in range (n)]
    
    if nums[0] == 0 : 
        dp[0][0] = 2 
    else : dp[0][0] = 1 
    
    if nums[0] != 0 and nums[0] <= tar: 
        dp[0][nums[0]] = 1 
        
    for ind in range (1,n): 
        for target in range (tar +1): 
            notTaken = dp[ind - 1 ][target]
            
            taken = 0 
            if nums[ind] <= target: 
                taken = dp[ind - 1][target - nums[ind]]
            dp[ind][target] = (notTaken + taken) % MOD 
    return dp[n-1][tar]


# Space Optimization 
def targetSum (nums,target):
    totalSum = 0 
    for i in range (len(nums)): 
        totalSum += nums[i] 
        
    if (totalSum - target) < 0 or ((totalSum - target) % 2): 
        return 0 
    
    return helper(nums,(totalSum - target) // 2 )


def helper(nums,tar):
    n = len(nums) 
    prev = [0 for i in range (tar+1)]
    
    if nums[0] == 0: 
        prev[0] = 2 
    else: 
        prev[0] = 1 
    if nums[0] != 0 and nums[0] <= tar: 
        prev[nums[0]] = 1 
        
    for ind in range (1,n): 
        curr = [0 for i in range (tar +1)]
        for target in range (tar +1):
            notTaken = prev[target]
            
            taken = 0 
            if nums[ind] <= target: 
                taken = prev[target - nums[ind]]
            curr[target] = (notTaken + taken) % MOD 
        prev = curr 
    return prev[tar]    
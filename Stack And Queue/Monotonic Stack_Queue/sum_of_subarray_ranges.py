'''

LeetCode :> https://leetcode.com/problems/sum-of-subarray-ranges/description/

You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.
 

Constraints:

1 <= nums.length <= 1000
-109 <= nums[i] <= 109
 

Follow-up: Could you find a solution with O(n) time complexity?


'''

# Brute Force 

def subRange(nums):
    
    n = len(nums)
   
    sumA = 0
    
    for i in range (n):
        miniA = nums[i] 
        maxA = nums[i] 
        
        for j in range (i,n):
            miniA = min(miniA,nums[j])
            maxA= max(maxA,nums[j])
            
            sumA += (maxA - miniA)            
    return sumA


# Optimal Approach 
def optimalSum(nums):
    
    n = len(nums)
    stack = []
    result = 0

        # Calculate contribution of minimums
    for i in range(n + 1):
        while stack and (i == n or nums[stack[-1]] > nums[i]):
            j = stack.pop()
            k = stack[-1] if stack else -1
            result -= nums[j] * (i - j) * (j - k)
        stack.append(i)

    stack.clear()

        # Calculate contribution of maximums
    for i in range(n + 1):
        while stack and (i == n or nums[stack[-1]] < nums[i]):
            j = stack.pop()
            k = stack[-1] if stack else -1
            result += nums[j] * (i - j) * (j - k)
        stack.append(i)

    return result
    
    
    
    
    
    
    
    

# a = [1,2,3]
a = [4,-2,-3,4,1]
# print(subRange(a))
print(optimalSum(a))
'''
LeetCode :> https://leetcode.com/problems/sliding-window-maximum/description/

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length

'''
# Brute Force 
from collections import deque


def eachMaxx(nums,k):
    n = len(nums)
    stack = []
    
    for i in range(n - k + 1):
        maxi = float("-inf")
        for j in range (i,i +k):
            if nums[j] > maxi :
                maxi = nums[j] 
        stack.append(maxi)
                
    return stack


# Optimal Approach 
def maxSliding(nums,k):
    dq = deque() 
    ans = [] 
    
    for i in range (len(nums)):
        if dq and dq[0] == i - k :
            dq.popleft() 
            
        while dq and nums[dq[-1]] < nums[i] :
            dq.pop() 
        dq.append(i)
        
        
        if i >= k -1 : 
            ans.append(nums[dq[0]])

    return ans 


a = [1,3,-1,-3,5,3,6,7]
k = 3
print(eachMaxx(a,k))
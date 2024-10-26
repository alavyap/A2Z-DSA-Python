'''

LeetCode :> https://leetcode.com/problems/binary-subarrays-with-sum/description/

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of the array.

 

Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
Example 2:

Input: nums = [0,0,0,0,0], goal = 0
Output: 15
 

Constraints:

1 <= nums.length <= 3 * 104
nums[i] is either 0 or 1.
0 <= goal <= nums.length

'''

def sumSub(nums, goal):
    mpp = {0:1}
    pre_sum = 0 
    count = 0 
    
    
    for num in nums :
        pre_sum +=  num 
        
        if (pre_sum - goal) in mpp:
            count += mpp[pre_sum - goal]
            
        mpp[pre_sum ] = mpp.get(pre_sum,0 ) +1
    return count
            



# a = [1,0,1,0,1] 
a = [0,0,0,0,0] 
g = 0
print(sumSub(a,g))
            
            
        